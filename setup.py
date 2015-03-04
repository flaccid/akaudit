#!/usr/bin/env python

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
        description = "Audit who has access to your homes.",
        license = "Apache 2.0",
        url = "https://github.com/flaccid/akaudit",
        scripts=['bin/akaudit'],
        packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
        install_requires = ['paramiko', 'colorama'] + opt_requires,
        )
