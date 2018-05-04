#!/usr/bin/env python

from distutils.core import setup

# get version
from wraptor import __version__

setup(
    name='Wraptor',
    version=__version__,
    author='Carl Sverre',
    author_email='carl@carlsverre.com',
    url='http://github.com/carlsverre/wraptor',
    license='LICENSE.txt',
    description='Useful decorators and other utility functions.',
    long_description=open('README.rst').read(),
    packages=[
        'wraptor',
        'wraptor.decorators',
        'wraptor.context',
    ],
)
