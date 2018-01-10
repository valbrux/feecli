#!/usr/bin/env python3
from distutils.core import setup

version = ['0','0','1']

setup(name='feecli',
        version=".".join(version),
        description='Feedly terminal client',
        author='Valerio Brussani',
        author_email='valerio.brussani@gmail.com',
        platforms=["linux"],
        scripts=['scripts/feecli',]
)
