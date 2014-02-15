#!/bin/bash
#
# Copyright (C) 2013 Codethink Limited
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


set -e

cd ~
git clone --depth=1 -b master https://github.com/libgit2/libgit2.git
ls .
cd libgit2
mkdir build
cd build
cmake .. \
  -DCMAKE_INSTALL_PREFIX=../_install \
  -DBUILD_CLAR=OFF \
  -DBUILD_SHARED_LIBS:BOOLEAN=OFF
cmake --build . --target install
ls ..
