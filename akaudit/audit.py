import os.path
import sys
import pwd, grp
import logging
from paramiko import SSHClient, SSHConfig
from colorama import Fore, Back, Style

class Auditer():
    def run_audit(self, args):
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
                        sys.stdout.write(Fore.RESET + Back.RESET + Style.RESET_ALL)
        sys.exit()