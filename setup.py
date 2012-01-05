#!/usr/bin/env python
# Copyright (C) 2012 Eli Golovinsky <eli.golovinsky@gmail.com>.
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

from distutils.core import setup

DESCRIPTION = """
Provides an inline interactive menu for selecting files / branches / hashes
when running the git command line interface and stays out of the way.
"""

setup(
    name='Gitter',
    version='0.1.0',
    description='Interactive in-line menus for Unix-based terminals',
    long_description=DESCRIPTION,
    author='Eli Golovinsky',
    license='GPL',
    author_email='eli.golovinsky@gmail.com',
    url='https://github.com/gooli/Gitter',
    scripts=['gitter'],
    classifiers=[
        'Development Status :: Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Terminals'
    ],
    requires=['termenu (>=0.3.0)'],
)

