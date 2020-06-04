#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='beautiful_barcode',
      version='1.0.0',
      description='Generate nicely formatted barcodes (UPC-A)',
      author='Boxine GmbH',
      author_email='it@boxine.de',
      packages=['beautiful_barcode'],
      license='MIT',
      url='https://github.com/boxine/beautiful_barcode/')
