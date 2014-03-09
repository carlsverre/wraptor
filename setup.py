#!/usr/bin/env python

from distutils.core import setup
from setuptools.command.test import test as TestCommand

# get version
from wraptor import __version__

class PyTest(TestCommand):
    user_options = [
        ('watch', 'w',
         "watch tests for changes"),
        ('pdb', 'i',
         "start pdb on failures"),
        ('scan=', 's',
         "only search for tests in the specified directory or file"),
        ('exitfirst', 'x',
         "Stop tests on first failure"),
        ('expression=', 'k',
         "Only run tests matching given expression"),
    ]
    boolean_options = ['watch', 'pdb', 'exitfirst']

    def initialize_options(self):
        self.watch = False
        self.pdb = False
        self.scan = None
        self.exitfirst = False
        self.expression = None
        self.test_suite = None
        self.test_module = None
        self.test_loader = None

    def finalize_options(self):
        TestCommand.finalize_options(self)

        self.test_suite = True
        self.test_args = ['-v']
        if self.watch:
            self.test_args.append('-f')
        if self.pdb:
            self.test_args.append('--pdb')
        if self.exitfirst:
            self.test_args.append('-x')
        if self.expression:
            self.test_args.extend(['-k', self.expression])
        if self.scan is not None:
            self.test_args.append(self.scan)
        else:
            self.test_args.append('wraptor')

    def run_tests(self):
        import os, sys, glob

        MY_PATH = os.path.dirname(__file__)
        sys.path.append(MY_PATH)
        os.environ['PYTHONPATH'] = os.environ.get('PYTHONPATH', '') + ':' + MY_PATH

        egg_dirs = glob.glob('*.egg')
        ignore_args = ['--ignore=%s' % d for d in egg_dirs]

        import pytest
        errno = pytest.main(ignore_args + self.test_args)
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
