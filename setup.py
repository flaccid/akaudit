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

try:
    import pkg_resources
    import setuptools
except ImportError:
    # Import setuptools if it's not already installed
    import distribute_setup
    distribute_setup.use_setuptools()

import os
import sys
from setuptools import setup
from setuptools import find_packages

import akaudit

opt_requires = []
# argparse is built-in in py2.7+ and py3.2+
if (sys.version_info[:2][0] < 3 and sys.version_info[:2][1] < 7) or (sys.version_info[:2][0] >= 3 and sys.version_info[:2][1] < 2):
    opt_requires.append('argparse')

setup(
    name = "akaudit",
    version = akaudit.__version__,
    author = "Chris Fordham",
    author_email = "chris@fordham-nagy.id.au",
    description = akaudit.__description__,
    license = "Apache 2.0",
    url = "https://github.com/flaccid/akaudit",
    download_url = 'https://github.com/flaccid/akaudit/tarball/v' + akaudit.__version__,
    scripts=['bin/akaudit'],
    packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires = ['paramiko', 'colorama', 'six'] + opt_requires,
)
