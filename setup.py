#!/usr/bin/env python

from distutils.core import setup
from setuptools.command.test import test as TestCommand

# get version
from wraptor import __version__

class PyTest(TestCommand):
    user_options = [
        ('watch', 'w',
         "watch tests for changes"),
        ('scan-directory=', 'd',
         "only search for tests in the specified directory"),
    ]
    boolean_options = ['watch']

    def initialize_options(self):
        self.watch = False
        self.scan_directory = None
        self.test_suite = None
        self.test_module = None
        self.test_loader = None

    def finalize_options(self):
        TestCommand.finalize_options(self)

        self.test_suite = True
        self.test_args = []
        if self.watch:
            self.test_args.append('-f')
        if self.scan_directory is not None:
            self.test_args.append(self.scan_directory)

    def run_tests(self):
        import os, sys

        MY_PATH = os.path.dirname(__file__)
        sys.path.append(MY_PATH)
        os.environ['PYTHONPATH'] = os.environ.get('PYTHONPATH', '') + ':' + MY_PATH

        import pytest
        errno = pytest.main(self.test_args)
        raise sys.exit(errno)

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
        'wraptor.test',
        'wraptor.decorators',
        'wraptor.decorators.test',
        'wraptor.context',
        'wraptor.context.test',
    ],
    tests_require=['pytest'],
    cmdclass={ 'test': PyTest },
)
