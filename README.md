# akaudit

Audit who has SSH access to your user homes via authorized_keys.

## Installation

See INSTALL.md.

## Usage

For help on usage:

    $ akaudit --help

Audit your system with current user's access level:

    $ akaudit   

Audit the entire system (recommended):

	# akaudit

Audit the entire system in interactive mode which prompts removal of each key:

	# akaudit -i

Audit with debug log level (recommended until first major release):

	$ akaudit -l debug

## License

- Author: Chris Fordham (<chris@fordham-nagy.id.au>)

```text
Copyright 2011-2019, Chris Fordham

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
