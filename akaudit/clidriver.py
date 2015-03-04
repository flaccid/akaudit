#!/usr/bin/env python

import sys
import argparse
from akaudit.audit import Auditer

def main(argv = sys.argv, log = sys.stderr):
	parser = argparse.ArgumentParser(description='Audit who has access to your homes.', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-l', '--log', default='info', help='Log level')
	args = parser.parse_args()
	auditer = Auditer()
	auditer.run_audit(args)

if __name__ == "__main__":
    main(sys.argv[1:])
