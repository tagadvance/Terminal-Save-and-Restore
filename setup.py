#!/usr/bin/env python3.6

from setuptools import setup, find_packages

setup(
    name='Terminal-Save-and-Restore',
    version='1.0',
    description='',
    author='Tag',
    author_email='tagadvance+Terminal-Save-and-Restore@gmail.com',
    url='https://github.com/tagadvance/Terminal-Save-and-Restore',
    packages=find_packages(),
    install_requires=[
        'nose',
        'coverage'
    ]
)