#!/usr/bin/env python
# coding=utf-8

from abc import abstractmethod

class Fruit(object):
    @abstractmethod
    def __init__(self):
        pass
    def __str__(self):
        pass

    @abstractmethod
    def growth(self):
        pass

    @abstractmethod
    # 'Note the usage of @abstractmethod'
    def eat(self):
        pass

class Apple(Fruit):
    def __init__(self):
        self.name = 'Apple'
    def __str__(self):
        print('Fruit is {}'.format(self.name))
    def growth(self):
        print('Apple growth')
    def eat(self):
        print('Apple were eaten')

class Facade(object):
    '''
    By using this class to integrate functions together.
    Therefore in main() we just need to consider interface provided here
    '''
    def __init__(self):
        self.apple = Apple()
    def create_growth(self, fruittype = 'Apple'):
        if fruittype == 'Apple':
            self.apple.growth()
        else:
            pass

def main():
    apple = Facade()
    apple.create_growth()

if __name__ == '__main__':
    main()


