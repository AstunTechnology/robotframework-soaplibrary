#!/usr/bin/env python
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


"""Setup script for robotframework-soaplibrary for Robot Framework"""

from distutils.core import setup

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from SoapLibrary import __version__

def main():
    setup(name         = 'robotframework-soaplibrary',
          version      = __version__,
          description  = 'SoapLibrary Testing Keywords for using zeep with the Robot Framework',
          author       = 'Astun Technology',
          author_email = '',
          url          = '',
          package_dir  = { '' : 'src'},
          packages     = ['SoapLibrary'],
          install_requires = [
              'robotframework >= 3.0.0'
              'zeep >= 3.1.0'
          ]
          )


if __name__ == "__main__":
    main()
