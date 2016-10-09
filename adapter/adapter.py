#!/usr/bin/env python
# coding=utf-8
class Cat:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return '{} the cat'.format(self.name)
    def speak(self):
        return 'Miaow'

class Human:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return '{} the human'.format(self.name)
    def say(self):
        return 'hello'

class Adapter:
    def __init__(self, obj, adapted_method):
        self.obj = obj
        self.__dict__.update(adapted_method)
    def __str__(self):
        return str(self.obj)

def main():
    objects = [Cat('kitty')]
    humanbeing = Human('john')
    objects.append(Adapter(humanbeing, dict(speak=humanbeing.say)))
    for i in objects:
        print('{} {}'.format(i,i.speak()))
    return objects

if __name__ == '__main__':
    objects = main()





