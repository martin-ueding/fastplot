#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2014 Martin Ueding <martin-ueding.de>

from setuptools import setup, find_packages

setup(
    author="Martin Ueding",
    description="Plots some data files",
    license="GPL2",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python",
    ],
    name="fastplot",
    packages=find_packages(),
    scripts=[
        'fastplot',
    ],
    install_requires=[
        'matplotlib',
        'numpy',
    ],
    url="https://github.com/martin-ueding/fastplot",
    download_url="http://martin-ueding.de/download/fastplot/",
    version="1.0",
)
