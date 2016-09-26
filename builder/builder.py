#!/usr/bin/env python
# coding=utf-8

# Abstract builder
class AbstractBuilder(object):
    def add_a(self):
        pass
    def add_b(self):
        pass

# Discrete builder
class BuilderA(AbstractBuilder):
    def __init__(self):
        self.product = []
    def add_a(self):
        self.product.append('a_a')
    def add_b(self):
        self.product.append('a_b')
    def __str__(self):
        result = ''
        for i in self.product:
            result += 'product:'+i+''
        return result

class BuilderB(AbstractBuilder):
    def __init__(self):
        self.product = []
    def add_a(self):
        self.product.append('b_a')
    def add_b(self):
        self.product.append('b_b')
    def __str__(self):
        result = ''
        for i in self.product:
            result += 'product:'+i+''
        return result


# Director
def director(builder):
    builder.add_a()
    builder.add_b()

if __name__ == '__main__':
    builder_a = BuilderA()
    builder_b = BuilderB()

    director(builder_a)
    print builder_a

    director(builder_b)
    print builder_b
