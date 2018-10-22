"""Setup script for SoapLibrary for Robot Framework"""

from distutils.core import setup

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from SoapLibrary import __version__

def main():
    setup(name         = 'SoapLibrary',
          version      = __version__,
          description  = 'iShare SOAP Testing Keywords for Robot Framework',
          author       = 'Astun Technology',
          author_email = '',
          url          = '',
          package_dir  = { '' : 'src'},
          packages     = ['SoapLibrary'],
          )


if __name__ == "__main__":
    main()
