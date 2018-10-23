#!/usr/bin/env python

import os
import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), 'src'))
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup

execfile(join(dirname(__file__), 'src', 'SoapLibrary', 'version.py'))

DESCRIPTION = """
SoapLibrary is a web service testing library for Robot Framework
that leverages zeep to test SOAP-based services.
""".strip()

CLASSIFIERS  = """
Development Status :: 5 - Development
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
""".strip().splitlines()

import zeep

setup(name         = 'robotframework-soaplibrary',
      version      = VERSION,
      description  = 'Robot Framework test library for SOAP-based services using zeep.',
      long_description = DESCRIPTION,
      author       = 'Astun Technology',
      author_email = '<developers@astuntechnology.com>',
      url          = 'https://github.com/AstunTechnology/robotframework-soaplibrary',
      license      = 'Apache License 2.0',
      keywords     = 'robotframework testing testautomation soap zeep web service',
      platforms    = 'any',
      classifiers  = CLASSIFIERS,
      zip_safe     = True,
      install_requires = [
                            'zeep >= 3.1.0',
                            'robotframework >= 3.0.0',
                         ],
      package_dir  = {'' : 'src'},
      packages     = ['SoapLibrary']
      )