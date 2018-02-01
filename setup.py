#!/usr/bin/env python

#
# Copyright (c) 2013, Digium, Inc.
#

"""Setup script
"""

import os

from setuptools import setup

setup(
    name="swaggerpython",
    version="0.2.2",
    license="BSD 3-Clause License",
    description="Library for accessing Swagger-enabled API's",
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       "README.rst")).read(),
    author="Digium, Inc and Infectious Media",
    author_email="sre@infectiousmedia.com",
    url="https://github.com/poogles/swagger-python",
    packages=["swaggerpython"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    tests_require=["nose", "tissue", "coverage", "httpretty"],
    install_requires=["requests", "websocket-client", "six", "httpretty"],
    entry_points="""
    [console_scripts]
    swagger-codegen = swaggerpython.codegen:main
    """
)
