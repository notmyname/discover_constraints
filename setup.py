#!/usr/bin/python

from setuptools import setup, find_packages


setup(name='discover_constraints', version='1.0.0',
    description='Discover Constraints Middleware', author='SwiftStack',
    url='https://swiftstack.com/', packages=find_packages(),
    classifiers=['Development Status :: 4 - Beta',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.6',
                 'Environment :: No Input/Output (Daemon)'],
    entry_points={'paste.filter_factory':
                    ['discover_constraints=middleware:filter_factory']})
