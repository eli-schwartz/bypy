#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: GPLv3 Copyright: 2016, Kovid Goyal <kovid at kovidgoyal.net>

import os

from bypy.constants import PREFIX, PYTHON, build_dir, iswindows
from bypy.utils import python_install, replace_in_file, run

if iswindows:
    def main(args):
        replace_in_file('setup.py', '2019', '2020')
        run(
            PYTHON, 'setup.py', 'fetch', '--all',
            '--missing-checksum-ok', 'build', 'install', '--root', build_dir()
        )
        python_install()


def install_name_change_predicate(x):
    return x.endswith('apsw.so')


def install_name_change(old_name, is_dep):
    bn = os.path.basename(old_name)
    if bn.startswith('libsqlite'):
        return os.path.join(PREFIX, 'lib', bn)
    return old_name
