#!/usr/bin/env python

import os
import sys
import stat
import itertools
import termcolor

try:
    import simplejson as json
except ImportError:
    import json

def tableize(data):
    """
    Takes a 2D list and makes a table of data
    """
    return '\n'.join('\t'.join(str(c) for c in r) for r in data)

def test(*args):

    if not args:
        return False
    if len(args) == 1:
        test_type = None
        test_input1 = args[0]
    if len(args) == 2:
        test_type = args[0]
        test_input1 = args[1]
    if len(args) == 3:
        test_input1 = args[0]
        test_type = args[1]
        test_input2 = args[2]

    if test_type == '-n' or test_type is None:
        return len(str(test_input1)) != 0
    if test_type == '-z':
        return len(str(test_input1)) == 0
    if test_type == '=':
        return str(test_input1) == str(test_input2)
    if test_type == '!=':
        return str(test_input1) != str(test_input2)
    if test_type == '-eq':
        return int(test_input1) == int(test_input2)
    if test_type == '-ge':
        return int(test_input1) >= int(test_input2)
    if test_type == '-gt':
        return int(test_input1) > int(test_input2)
    if test_type == '-le':
        return int(test_input1) <= int(test_input2)
    if test_type == '-lt':
        return int(test_input1) < int(test_input2)
    if test_type == '-ne':
        return int(test_input1) != int(test_input2)
    if test_type == '-ef':
        return (os.stat(test_input1).st_ino == os.stat(test_input2).st_ino and
                os.stat(test_input1).st_dev == os.stat(test_input2).st_dev)
    if test_type == '-nt':
        return os.stat(test_input1).st_mtime > os.stat(test_input2).st_mtime
    if test_type == '-ot':
        return os.stat(test_input1).st_mtime < os.stat(test_input2).st_mtime
    if test_type == '-nt':
        return os.stat(test_input1).st_mtime > os.stat(test_input2).st_mtime
    if test_type == '-b':
        return stat.S_ISBLK(os.stat(test_input1).st_mode)
    if test_type == '-c':
        return stat.S_ISCHR(os.stat(test_input1).st_mode)
    if test_type == '-d':
        return os.path.isdir(test_input1)
    if test_type == '-e':
        return os.path.isfile(test_input1)
    if test_type == '-f':
        return stat.IS_IFREG(os.stat(test_input1).st_mode)


def ls(dirname='.', all=None, do_print=True, long=False):
    def colorize_directories(directories):
        return ['{}/'.format(termcolor.colored(d, color='blue', attrs=['bold'])) for d in directories]
    def colorize_files(files):
        return ['{}*'.format(termcolor.colored(f, color='green', attrs=['bold'])) if os.access('{}/{}'.format(dirname, f), os.X_OK) else f for f in files]
    def permission_string(filename):
        output = 'd' if os.isdir(filename) else '-'
        #perms =
    for _, directories, files in os.walk(dirname):
        break
    if all is True:
        directories = ['.', '..'] + directories
    elif all is False:
        directories = [d for d in directories if not d.startswith('.')]
        files = [f for f in files if not f.startswith('.')]
    directories = sorted(directories, key=lambda x: x.lstrip('.'))
    files = sorted(files, key=lambda x: x.lstrip('.'))
    if do_print:
        colorized_directories = colorize_directories(directories)
        colorized_files = colorize_files(files)
        if not long:
            for cd in colorized_directories:
                print '{} '.format(cd),
            for cf in colorized_files:
                print '{} '.format(cf),
            print
        #else:
        #    tablize(rows)
    return directories, files

if __name__ == '__main__':
    ls()
    print
    ls(all=True)
