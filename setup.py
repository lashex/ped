# Copyright 2013 Gridward LLC
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import os
from distutils.core import setup
from setuptools import find_packages

version = '0.2.8'
README = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(README).read()

setup(name='plantextract',
      version=version,
      description='Python Plant Extract Document processor',
      long_description = long_description,
      author='Brett Francis',
      url='https://github.com/lashex/ped.git',
      packages=['plantextract'],
      # packages=find_packages(),
      include_package_data=True,
      license='Apache License, Version 2.0',
      install_requires=['lxml == 3.0.1'],
      keywords = "sunspec plant extract",
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Other Audience',
                   'Natural Language :: English',
                   'Programming Language :: Python',
                   'Topic :: Utilities',
                   'Topic :: Software Development',
                   'Topic :: Text Processing :: Markup :: XML',
                   'Operating System :: OS Independent',],
      )