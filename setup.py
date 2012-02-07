#!/usr/bin/env python

from distutils.core import setup
from simpleweb import __version__, __license__

setup(name='simpleweb.py',
      version=__version__,
      description='simpleweb.py: a simple web application framework',
      author='Jake Kupersmith',
      author_email='jakerosoft@gmail.com',
      maintainer='Jake Kupersmith',
      maintainer_email='jakerosoft@gmail.com',
      url='http://simpleweb.jackup.us/',
      packages=['simpleweb'],
      long_description='A simple web application framework',
      license=__license__,
      platforms=['any'],
      )
