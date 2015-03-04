#!/usr/bin/env python

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

import sys
import argparse
import akaudit
from akaudit.audit import Auditer

def main(argv = sys.argv, log = sys.stderr):
	parser = argparse.ArgumentParser(description=akaudit.__description__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('-l', '--log', default='info', help='log level')
	parser.add_argument('-i', '--interactive', help='interactive mode (prompts asking if to delete each key)', action="store_true")
	parser.add_argument('-v', '--version', action="version", version='%(prog)s ' + akaudit.__version__)
	args = parser.parse_args()

	auditer = Auditer()
	auditer.run_audit(args)

if __name__ == "__main__":
    main(sys.argv[1:])
