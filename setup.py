#!/usr/bin/env python
# flake8: noqa

from distutils.core import setup
from setuptools.command.test import test as TestCommand

# get version
with open('wraptor/__init__.py') as f:
    exec(f.read())

class PyTest(TestCommand):
    user_options = [
        ('watch', 'w',
         "watch tests for changes"),
    ]
    boolean_options = ['watch']

    def initialize_options(self):
        self.watch = False
        self.test_suite = None
        self.test_module = None
        self.test_loader = None

    def finalize_options(self):
        TestCommand.finalize_options(self)

        self.test_suite = True
        self.test_args = []
        if self.watch:
            self.test_args.append('-f')

    def run_tests(self):
        import pytest, sys
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
    cmdclass={ 'test': PyTest },
)
