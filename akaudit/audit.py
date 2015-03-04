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
import pwd, grp
import logging
import akaudit.keytools
from paramiko import SSHClient, SSHConfig
from colorama import Fore, Back, Style
from akaudit.userinput import yesno
from akaudit.keytools import remove_public_key

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

        config = SSHConfig()
        config.parse(open('/etc/ssh/sshd_config'))

        # TODO: check .ssh/authorized_keys2

        if 'authorizedkeysfile' in config.lookup(''):
            authorized_keys_file = config.lookup('')['authorizedkeysfile']
        else:
            authorized_keys_file = '.ssh/authorized_keys'

        logging.debug(str('sshd accepts keys in ' + authorized_keys_file + ' for users.'))

        for p in pwd.getpwall():
            if p[6] not in invalid_shells:
                home_dir = p[5]
                ak_path = os.path.join(home_dir, authorized_keys_file)
                if os.path.isfile(ak_path):
                    logging.info(str(p[0] + ' has authorized public keys!'))
                    logging.debug(str('user: ' + p[0] + ', shell: ' + p[6] + ', home: ' +  p[5]))
                    lines = [line.strip() for line in open(ak_path) if line.strip()]
                    for line in lines:
                        logging.debug(Fore.YELLOW + str(line.split()))
                        public_key = line.split()[1]
                        if len(line.split()) > 2:
                            label = line.split()[2]
                        else:
                            label = '<no label>'
                        print(ak_path, ':', label, ':', public_key[0:12] + '...' + public_key[-19:])
                        if args.interactive:
                            if yesno('==> Remove key? '):
                                remove_public_key(ak_path, public_key)
                                logging.info(Fore.GREEN + "Key '" + label + "' removed.")
                            else:
                                logging.debug(Fore.GREEN + "Key removal of '" + label + "' skipped.")
                            sys.stdout.write(Fore.RESET + Back.RESET + Style.RESET_ALL)

                        sys.stdout.write(Fore.RESET + Back.RESET + Style.RESET_ALL)
        sys.exit()
