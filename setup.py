# /usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. codeauthor:: Cédric Dumay <cedric.dumay@gmail.com>

"""
from setuptools import setup, find_packages

setup(
    name='logging-ldp',
    version=open('VERSION', 'r').read().strip(),
    description="OVH library bundle to send logs on Log Data Platform (LDP)",
    long_description=open('README.rst', 'r').read().strip(),
    classifiers=["Programming Language :: Python"],
    keywords='',
    author='Cedric DUMAY',
    author_email='cedric.dumay@gmail.com',
    url='https://github.com/cdumay/logging-ldp',
    license='Apache License 2.0',
    py_modules=['logging_ldp'],
    include_package_data=True,
    zip_safe=True,
    install_requires=open('requirements.txt', 'r').readlines(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
