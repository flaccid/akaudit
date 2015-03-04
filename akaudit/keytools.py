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

def remove_public_key(ak=None, key=None, dry=False):
	f = open(ak, 'r')
	lines = f.readlines()
	f.close()
	if not dry:
		f = open(ak, 'w')
		for line in lines:
			if key not in line:
				f.write(line)
		f.close()
