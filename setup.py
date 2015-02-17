#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import fishbone
version = fishbone.__version__

setup(
    name='fishbone',
    version=version,
    author="Mohamed Termoul",
    author_email='mtermoul@gmail.com',
    packages=[
        'fishbone',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.4',
    ],
    zip_safe=False,
    scripts=['fishbone/manage.py'],
)
