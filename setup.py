# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='range_utils',
      version='0.1.2',
      description='Some basic stuff for working with date ranges',
      url='http://github.com/bdomars/range_utils',
      author='Björn Domars',
      author_email='bdomars@abo.fi',
      license='MIT',
      packages=['range_utils'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
