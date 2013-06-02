#!env python

from distutils.core import setup
from setuptools.command.test import test as TestCommand

# get version
with open('wraptor/__init__.py') as f:
    exec(f.read())

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest, sys
        errno = pytest.main(self.test_args)
        raise sys.exit(errno)

setup(
    name='Wraptor',
    version='0.1.0',
    author='Carl Sverre',
    author_email='carl@carlsverre.com',
    packages=['wraptor', 'wraptor.test', 'wraptor.decorators', 'wraptor.decorators.test'],
    url='http://github.com/carlsverre/wraptor',
    license='LICENSE.txt',
    description='Useful decorators and other utility functions.',
    long_description=open('README.rst').read(),
    tests_require=['pytest'],
    cmdclass = { 'test': PyTest },
)
