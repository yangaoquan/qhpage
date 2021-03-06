#! python

import sys
import os
import os.path

from setuptools import setup, find_packages

depends = []

setup(
    name = 'qhpage',
    version = '1.0',
    packages = find_packages(exclude=['fabfile', 'fabfile.*',
                                      'test.*', '*.test', '*.test.*',
                                      'tests.*', '*.tests', '*.tests.*']),

    zip_safe = False,

    entry_points = {
        'console_scripts': [
        ],
    },

    install_requires = depends,

    dependency_links = [
        #"http://peak.telecommunity.com/snapshots/"
    ],
    
    include_package_data = True,

    long_description = 'scrapy v1.',
    
    description = "Scrapy v1 ."
)
