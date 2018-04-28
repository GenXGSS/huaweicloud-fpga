# Copyright 2017 Huawei Technologies Co., Ltd.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from setuptools import setup, find_packages

long_description = 'fisclient is a command-line client for \
FIS (FPGA Image Service) that brings the command set for \
FPGA image management together in a single shell'''

requires = [
    'keystoneauth1==2.18.0',
    'stevedore==1.19.1',
    'positional==1.1.1',
    'requests==2.13.0',
    'warlock==1.2.0',
    'jsonschema==2.5.1',
    'vcversioner==2.16.0.0',
    'functools32==3.2.3-2',
    'jsonpatch==1.14',
    'jsonpointer==1.10',
    'oslo.utils==3.18.0',
    'netifaces==0.10.4',
    'netaddr==0.7.18',
    'debtcollector==1.10.0',
    'wrapt==1.10.6',
    'monotonic==1.1',
    'iso8601==0.1.11',
    'funcsigs==0.4',
    'oslo.i18n==3.4.0',
    'pyparsing==2.2.0',
    'Babel==1.3',
    'pytz==2017.2',
    'prettytable==0.7.2',
    'six==1.9.0',
    'pbr==1.8.1',
]

setup(
    name='fisclient',
    version='1.2.0',
    description='FIS API Client',
    long_description=long_description,
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: FPGA Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
    packages=find_packages(exclude=['data']),
    zip_safe=True,
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'fisclient=fisclient.wrapshell:main',
            'fis=fisclient.cmdshell:main',
            'fischeck=fisclient.fischeck:main',
            'fisconfig=fisclient.fisconfig:main'
        ]
    }
)
