#!/usr/bin/env python

from setuptools import setup
import muffle

setup(
    name='muffle',
    version=str(muffle.__version__),
    description='silence output from external process',
    author='freeman-lab',
    author_email='the.freeman.lab@gmail.com',
    url='https://github.com/freeman-lab/muffle',
    long_description=open('README.md').read()
)
