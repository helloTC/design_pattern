#!/usr/bin/env python
# coding=utf-8
import copy
from collections import OrderedDict

class Book:
    def __init__(self, name, authors, prices, **rest):
        self.name = name
        self.authors = authors
        self.prices = prices
        self.__dict__.update(rest)
    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}:{}'.format(i, ordered[i]))
            if i == 'prices':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)

class Prototype:
    def __init__(self):
        self.objects = dict()
    def register(self, identifier, obj):
        self.objects[identifier] = obj
    def unregister(self, identifier):
        del self.objects[identifier]
    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier:{}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

def main():
    b1 = Book('UB Su', ('hew', 'tony'), prices = 182, length = 228)
    prototype = Prototype()
    cid = 'first version'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name = 'Wells', prices = 122, length = 321)

    print(b1)
    print(b2)

if __name__ == '__main__':
    main()





