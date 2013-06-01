from distutils.core import setup

setup(
    name='Wraptor',
    version='0.1.0',
    author='Carl Sverre',
    author_email='carl@carlsverre.com',
    packages=['wraptor', 'wraptor.test'],
    url='http://github.com/carlsverre/wraptor',
    license='LICENSE.txt',
    description='Useful decorators and other utility functions.',
    long_description=open('README.rst').read(),
)
