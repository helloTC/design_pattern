#!/usr/bin/env python
# coding=utf-8

class people(object):
    def work(self):
        print('people working')
    def sleep(self):
        print('sleeping')
    def speak(self):
        print('speaking')

class manager(people):
    def work(self):
        print('manager working\n')

class teacher(people):
    def work(self):
        print('teacher working\n')

def executor(cls):
    inst_obj = cls()
    inst_obj.work()

def main():
    print('teacher:')
    executor(teacher)
    print('manager:')
    executor(manager)

if __name__ == '__main__':
    main()
     




