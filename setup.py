#!/usr/bin/python3
# Copyright (c) 2018 Davide Gessa
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from setuptools import find_packages
from setuptools import setup

setup(name='tezpy',
	version='0.1',
	description='Tezos python library',
	author='Davide Gessa',
	setup_requires='setuptools',
	author_email='gessadavide@gmail.com',
	url='https://github.com/dakk/tezpy',
	license='MIT',
	packages=['tezpy'],
	install_requires=open ('requirements.txt', 'r').read ().split ('\n')
)