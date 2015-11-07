#!/usr/bin/env python

from setuptools import setup
import muffle

setup(
    name='muffle',
    version=muffle.__version__,
    description='silence output from external process',
    author='freeman-lab',
    author_email='the.freeman.lab@gmail.com',
    packages=['muffle'],
    url='https://github.com/freeman-lab/muffle',
    long_description='See https://github.com/freeman-lab/muffle'
)
