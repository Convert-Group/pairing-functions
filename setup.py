#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# Package meta-data
NAME = 'pairing-functions'
DESCRIPTION = 'A collection of pairing functions'
URL = 'https://github.com/ConvertGroupLabs/pairing-functions'
EMAIL = 'tools@convertgroup.com'
AUTHOR = 'Convert Group Labs'
REQUIRES_PYTHON = '>=3.5.2'
VERSION = (0, 2, 1)

# What packages are required for this module to be executed?
REQUIRED = []

# What packages are required for test suite execution?
TESTS_REQUIRED = [
    'pytest',
    'pytest-cov'
]

# What packages are optional?
EXTRAS = {}


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name=NAME,
    version='.'.join(map(str, VERSION)),
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=["tests", "docs"]),
    install_requires=REQUIRED,
    tests_require=TESTS_REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT License',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
