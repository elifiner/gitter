#!/usr/bin/env python
# Copyright (C) 2012 Eli Finer <eli.finer@gmail.com>.
#
# This file is part of Gitter.
#
# Gitter is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option) any later
# version.
#
# Gitter is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Gitter.  If not, see <http://www.gnu.org/licenses/>.

import platform
from setuptools import setup

DESCRIPTION = """
A command line interface for git that shows interactive menus for files /
branches / hashes when appropriate and stays out of way the rest of the time.
"""

# get version without importing
for line in open('gitter'):
    if line.startswith('__version__ = '):
        exec(line)
        break
else:
    raise Exception("can't determine version")

bash_completion_path = '/etc/bash_completion.d'
if platform.system() == 'Darwin':
    bash_completion_path = '/usr/local/etc/bash_completion.d'

setup(
    name='gitter',
    version=__version__,
    description='Improved command line interface for git',
    long_description=DESCRIPTION,
    author='Eli Finer',
    license='GPL',
    author_email='eli.finer@gmail.com',
    url='https://github.com/elifiner/gitter',
    scripts=['gitter'],
    data_files=[(bash_completion_path, ['gitter-completion.bash'])],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Terminals'
    ],
    install_requires=['termenu'],
)
