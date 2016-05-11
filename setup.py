# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

requires = [
              'pyghmi',
            ]

setup(
    name = 'ipmisim',
    version = '0.7',
    maintainer = 'Rohit Yadav',
    maintainer_email = 'bhaisaab@apache.org',
    url = 'https://github.com/bhaisaab/ipmisim',
    description = "ipmisim is a fake ipmi server",
    long_description = "ipmisim is a fake ipmi server",
    platforms = ("Any",),
    license = 'ASL 2.0',
    packages = find_packages(),
    install_requires = requires,
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    entry_points="""
    [console_scripts]
    ipmisim = ipmisim.ipmisim:main
    """,
)
