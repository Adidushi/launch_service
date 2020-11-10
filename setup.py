#!/usr/bin/env python

from setuptools import setup

setup(name='launch_service',
    version='0.0.1',
    description='Executing launch files through services',
    author='Adi Bar Ilan',
    author_email='adi.perfetto@gmail.com',
    scripts=['launch_service/run_launch.py'],
    package_dir={'': 'src'}
    )
