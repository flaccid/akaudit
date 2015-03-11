# Copyright 2015 Chris Fordham
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function

import os.path
import sys
import platform
import pwd, grp
import logging
import base64
import akaudit.authorized_keys
import akaudit.keytools
from akaudit.authorized_keys import PublicKey
from paramiko import SSHClient, SSHConfig
from colorama import init, Fore, Back, Style
from akaudit.userinput import yesno
from akaudit.keytools import remove_public_key

# https://pypi.python.org/pypi/colorama
init(autoreset=True)

class Auditer():
    def run_audit(self, args):
        sys.stdout.write(Fore.RESET + Back.RESET + Style.RESET_ALL)

        # assuming loglevel is bound to the string value obtained from the
        # command line argument. Convert to upper case to allow the user to
        # specify --log=DEBUG or --log=debug
        numeric_level = getattr(logging, args.log.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % loglevel)
        logging.basicConfig(format='%(levelname)s: %(message)s', level=numeric_level)

        invalid_shells = ['/bin/false', '/sbin/nologin', '/usr/bin/nologin']

        # TODO: check .ssh/authorized_keys2

        if platform.system() == 'Darwin':
            authorized_keys_file = '.ssh/authorized_keys'
        elif os.path.isfile('/etc/ssh/sshd_config'):
            config = SSHConfig()
            config.parse(open('/etc/ssh/sshd_config'))
            if 'authorizedkeysfile' in config.lookup(''):
                authorized_keys_file = config.lookup('')['authorizedkeysfile']
            else:
                authorized_keys_file = '.ssh/authorized_keys'
        else:
            raise Exception('Cannot find a local sshd_config in commonly installed paths')

        logging.debug(str('sshd accepts keys in ' + authorized_keys_file + ' for users'))

        for p in pwd.getpwall():
            # mega debug
            # logging.debug(str('parsing user, ' + p[0]))
            if p[6] not in invalid_shells:
                home_dir = p[5]
                ak_path = os.path.join(home_dir, authorized_keys_file)
                if os.path.isfile(ak_path) and os.path.getsize(ak_path) > 0:
                    logging.info(str('interrogating user, ' + p[0]))
                    logging.debug(str('user: ' + p[0] + ', shell: ' + p[6] + ', home: ' +  p[5]))

                    lines = [line.strip() for line in open(ak_path) if line.strip()]

                    # iterate over each line in the authorized keys file
                    for line in lines:
                        logging.debug(str('processing line: ' + line))
                        # return immediately when line is prefixed with # (a comment)
                        if line.startswith('#'):
                            logging.debug('skipping line with comment')
                        else:
                            try:
                                public_key = PublicKey(line)
                                if public_key.comment == '':
                                    label = '<none>'
                                else:
                                    label = public_key.comment

                                logging.debug("* key = %r" % public_key)
                                logging.debug("  - prefix = %r" % public_key.prefix)
                                logging.debug("  - algo = %r" % public_key.algo)
                                logging.debug("  - comment = %r" % public_key.comment)
                                logging.debug("  - options = %r" % public_key.options)
                                key_material = base64.b64decode(public_key.blob.decode("utf-8"))
                                logging.debug("  - key_material = %r" % key_material)

                                logging.info('[key found] ' + ak_path + ':' + label + ':' + key_material[0:12] + '...' + key_material[-19:])
                            except ValueError as e:
                                logging.debug("* failure = %r" % e)

                            # for interactive mode, ask the user what to do with each detected key
                            if args.interactive:
                                if yesno('==> Remove key (y/n) ? '):
                                    remove_public_key(ak_path, key_material)
                                    logging.info(Fore.GREEN + "Key '" + label + "' removed.")
                                else:
                                    logging.debug(Fore.GREEN + "Key removal of '" + label + "' skipped.")
                                    if not logging.getLogger().isEnabledFor(logging.DEBUG):
                                        print()

        logging.info('audit complete.')
        sys.exit()
