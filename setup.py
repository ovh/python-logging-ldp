# /usr/bin/env python
# -*- coding: utf-8 -*-

# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
# Copyright 2019 The logging-gelf Authors. All rights reserved.

from setuptools import setup, find_packages

setup(
    name='logging-ldp',
    version=open('VERSION', 'r').read().strip(),
    description="OVH library bundle to send logs on Log Data Platform (LDP)",
    long_description=open('README.rst', 'r').read().strip(),
    classifiers=["Programming Language :: Python"],
    keywords='',
    author='OVH SAS',
    author_email='github@ovh.net',
    url='https://github.com/ovh/python-logging-ldp',
    license='BSD',
    py_modules=['logging_ldp'],
    include_package_data=True,
    zip_safe=True,
    install_requires=open('requirements.txt', 'r').readlines(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
