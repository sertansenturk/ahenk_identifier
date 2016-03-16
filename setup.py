#!/usr/bin/env python

from setuptools import setup

setup(name='ahenk-identifier',
    version='1.2',
    author='Sertan Senturk',
    author_email='contact AT sertansenturk DOT com',
    license='agpl 3.0',
    description='Identifies the ahenk (transposition) of a makam music recording given the tonic frequency and the symbol (or the makam)',
    url='http://sertansenturk.com',
    packages=['ahenkidentifier'],
    install_requires=[
        "numpy",
        "future",
    ],
)
