import sys
import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'checkmate'))
from version import VERSION

setup(name='checkmate',
      version=VERSION,
      description='A Python wrapper for the CheckMate REST API.',
      long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
      author='Ryan Eschinger',
      author_email='ryanesc@gmail.com',
      url='http://www.checkmate.io/',
      packages=['checkmate'],
      install_requires = ['requests >= 2.5.0', 'attrdict == 1.2.0']
      )
