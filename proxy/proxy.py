#!/usr/bin/env python
# coding=utf-8

class UserManager(object):
    def __init__(self):
        self.name = ['tony', 'god']

    def readinfo(self):
        print('{} users: {}'.format(len(self.name), ' '.join(self.name)))
    
    def adduser(self, username):
        self.name.append(username)
        print('Add user: {}'.format(username))

class ProtectProxy(object):
    def __init__(self):
        self.protectedproxy = UserManager()
        self.passwd = '123'
    
    def readinfo(self):
        self.protectedproxy.readinfo()
    
    def adduser(self, username, inputcode):
        if inputcode == self.passwd:
            self.protectedproxy.adduser(username)
        else:
            raise Exception('Wrong password')

    
if __name__ == '__main__':
    manager_machine = ProtectProxy()
    manager_machine.readinfo()
    manager_machine.adduser('mike', '123')


