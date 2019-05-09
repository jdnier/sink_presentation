#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='sink',
    version='0.1.0',
    description='Echo server that caches stdin and repeatedly writes it to a named pipe (FIFO).',
    author='David Niergarth',
    author_email='dniergarth@zendesk.com',
    url='https://github.com/jdnier/sink_presentation',
    packages=find_packages(),
    install_requires=[
        'fire',
    ],
    entry_points="""
        [console_scripts]
        sink=sink.sink:main
    """,
)
