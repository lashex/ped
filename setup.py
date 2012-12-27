import os
from distutils.core import setup
from setuptools import find_packages

version = '0.2.3'
README = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(README).read() + 'nn'

setup(name='plantextract',
      version=version,
      description='Python Plant Extract Document processor',
      long_description = long_description,
      author='Brett Francis',
      url='https://github.com/lashex/ped.git',
      packages=['plantextract'],
      # packages=find_packages(),
      include_package_data=True,
      install_requires=['lxml >= 3.0'],
      keywords = "sunspec plant extract",
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Other Audience',
                   'Natural Language :: English',
                   'Programming Language :: Python',
                   'Topic :: Utilities',],
      )