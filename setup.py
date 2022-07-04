"""
Author: Claire Baxter
Date: 04/07/2021
Description: Setup file to distribute the library

Adapted from https://stackoverflow.com/questions/62552631/module-not-recognising-root-directory-for-python-imports

See Also:
    * https://github.com/pypa/sampleproject
    * https://packaging.python.org/en/latest/distributing.html
    * https://pythonhosted.org/an_example_pypi_project/setuptools.html
"""
from setuptools import setup

setup(name='textkernel',
      version='0.0.1',
      # Specify packages (directories with __init__.py) to install.
      # You could use find_packages(exclude=['modules']) as well
      packages=['utils'],  # These need to have __init__.py
      include_package_data=True,
      )
