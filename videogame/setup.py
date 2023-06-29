#!/usr/bin/env python3
# Juan Uriarte
# uriarte.juan@csu.fullerton.edu
# uriartej

""" Simple setup.py """

from setuptools import setup

setup_info = {
    "name": "videogame",
    "version": "0.1",
    "description": "A package to support writing games with PyGame",
    "packages": ["videogame"],
    "install_requires": ["pygame"],
    # TODO: Optional, add more information to the setup.py script
    # "long_description": open("README.md").read(),
    # "author": "Tuffy Titan",
    # "author_email": "tuffy@csu.fullerton.edu",
    # "url": "https://some.url/somehwere/maybe/github",
}

setup(**setup_info)
