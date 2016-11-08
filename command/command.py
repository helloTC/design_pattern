#!/usr/bin/env python
# coding=utf-8

import os

verbose = 1
class RenameFile(object):
    def __init__(self, path_src, path_dst):
        self.src, self.dst = path_src, path_dst
    def execute(self):
        if verbose:
            print('Renaming {0} to {1}'.format(self.src, self.dst))
        os.rename(self.src, self.dst)
    def undo(self):
        if verbose:
            print('renaming {0} to {1}'.format(self.dst, self.src))
        os.rename(self.dst, self.src)

class DeleteFile(object):
    def __init__(self, path):
        self.path = path
    def execute(self):
        if verbose:
            print('Deleting {}'.format(self.path))
        os.remove(self.path)
    def undo(self):
        pass

class CreateFile(object):
    def __init__(self, path, text = 'hello, world\n'):
        self.path, self.text = path, text
    def execute(self):
        if verbose:
            print('Creating {0}'.format(self.path))
        with open(self.path, 'w') as out_file:
            out_file.write(self.text)
    def undo(self):
        delmethod = DeleteFile(self.path)
        delmethod.execute()

class OpenFile(object):
    def __init__(self, path):
        self.path = path
    def execute(self):
        if verbose:
            print('Opening file {}'.format(self.path))
        with open(self.path, 'r') as open_file:
            print(open_file.read())

def main():
    src_name, dst_name = 'file1', 'file2'

    commands = []
    for cmd in [CreateFile(src_name), OpenFile(src_name), RenameFile(src_name, dst_name)]:
        commands.append(cmd)
    [c.execute() for c in commands]

if __name__ == '__main__':
    main()

        
