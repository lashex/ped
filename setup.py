from distutils.core import setup
from setuptools import find_packages

setup(name='plantextract',
      version='0.1.0',
      description='Python Plant Extract Document processor',
      author='Brett Francis',
      packages=find_packages(),
      include_package_data=True,
      install_requires=["lxml >= 3.0"],
      keywords = "sunspec plant extract",
      )