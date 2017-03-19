# -*- coding: utf-8 -*-
#
# This file is part of the xkcd-get project
#
# Copyright (c) 2017 Tiago Coutinho
# Distributed under the MIT license. See LICENSE for more info.

import os
import sys
from setuptools import setup

requirements = [
    'grequests',
    'bs4',
]

setup(
    name='xkcd-get',
    version='0.0.2',
    description="downloader of xkcd comics",
    author="Tiago Coutinho",
    author_email='coutinhotiago@gmail.com',
    url='https://github.com/tiagocoutinho/xkcd',
    py_modules=['xkcd_get'],
    entry_points={
        'console_scripts': [
            'xkcd-get=xkcd_get:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='xkcd',
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
