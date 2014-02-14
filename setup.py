#!/usr/bin/env python
#
# Copyright (C) 2014 Jannis Pohlmann <jannis@xfce.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""Script to test, build and install consonant-annotator-store."""


import glob
import itertools
import os
import subprocess
import sys

from distutils.core import setup
from distutils.cmd import Command


class Check(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def _check_coding_style(self):
        sys.stdout.write('Checking coding style against PEP 8\n')
        subprocess.check_call(['pep8', '--statistics', '.'])

    def _check_docstrings(self):
        sys.stdout.write('Checking coding style against PEP 257\n')
        subprocess.check_call(['pep257', '.'])

    def _run_scenario_tests(self):
        sys.stdout.write('Running scenario tests\n')

        # collect files to include in the test suite
        yarn_dir = os.path.join('tests', 'yarn')
        patterns = [
            os.path.join(yarn_dir, '*'),
            os.path.join(yarn_dir, 'implementations', '*.yarn')
        ]
        globs = [glob.glob(x) for x in patterns]
        filenames = list(itertools.chain.from_iterable(globs))
        shell_lib = os.path.join(yarn_dir, 'implementations', 'helpers.sh')

        subprocess.check_call(['yarn', '-s', shell_lib] + filenames)

    def _check_copyright_years_and_license_headers(self):
        if os.path.isdir('.git'):
            sys.stdout.write('Collecting versioned files\n')
            files = subprocess.check_output(['git', 'ls-files']).splitlines()
            files.remove('COPYING')

            sys.stdout.write('Check copyright years\n')
            for filename in files:
                subprocess.check_call(
                    [os.path.join('scripts', 'check-copyright-year'),
                     '-v', filename])

            sys.stdout.write('Check license headers\n')
            for filename in files:
                subprocess.check_call(
                    [os.path.join('scripts', 'check-license-header'),
                     '-v', filename])

    def run(self):
        self._check_coding_style()
        self._check_docstrings()
        self._check_copyright_years_and_license_headers()
        #self._run_scenario_tests()


class Clean(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        pass


setup(
    name='consonant-annotator-store',
    long_description='''\
        consonant-annotator-store is a store backend for Annotator based \
        on Consonant. It is written in Python. \
        ''',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: '
        'License :: OSI Approved :: '
        'GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Version Control',
    ],
    author='Jannis Pohlmann',
    author_email='jannis@xfce.org',
    url='http://github.com/jannis/consonant-annotator-store',
    scripts=['consonant-annotator-store'],
    packages=[''],
    package_data={},
    data_files=[],
    cmdclass={
        'check': Check,
        'clean': Clean,
    })
