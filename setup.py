#!/usr/bin/env python env
# -*- coding:utf-8 -*-
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

about = {}

base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, "mceliece", "__about__.py")) as f:
    exec(f.read(), about)


with open(os.path.join(base_dir, "README.rst")) as f:
    long_description = f.read()

with open(os.path.join(base_dir, "CHANGES.txt")) as f:
    long_description = "\n".join([long_description, f.read()])




setup(
	name='mceliece',
    version=about["__version__"],

    description=about["__summary__"],
    long_description=long_description,
    license=about["__license__"],
    url="https://github.com/aburan28/mceliece",
    author=about["__author__"],
    author_email=about["__email__"],

	classifiers=[
	   'Development Status :: 3 - Alpha',
	    # Indicate who your project is intended for
	    'Intended Audience :: Developers',
	    'Topic :: Software Development :: Build Tools',

	    'Programming Language :: Python :: 2',
	    'Programming Language :: Python :: 2.6',
	    'Programming Language :: Python :: 2.7'
    ]
)
