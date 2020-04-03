# Encoding: utf-8

# --
# Copyright (c) 2008-2020 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --

from os import path

from setuptools import setup, find_packages


here = path.normpath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as long_description:
    LONG_DESCRIPTION = long_description.read()

setup(
    name='nagare-publishers-kafka',
    author='Net-ng',
    author_email='alain.poirier@net-ng.com',
    description='Kakfa publisher',
    long_description=LONG_DESCRIPTION,
    license='BSD',
    keywords='',
    url='https://github.com/nagareproject/publishers-kafka',
    packages=find_packages(),
    zip_safe=False,
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=['nagare-services-kafka', 'nagare-server'],
    entry_points='''
        [nagare.publishers]
        kafka = nagare.publishers.kafka_publisher:Publisher
    '''
)
