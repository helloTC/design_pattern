#!/usr/bin/env python
# coding=utf-8

"""
    Flyweight design pattern
    1 Learn this design pattern. 
    2 Consider realization of Tree carefully, especially for __new__
      It's a flexible method to design a dictionary for add or delete variables
    3 Note the usage of 'for _ in range() if we needn't a variable to loop

    Finally, Pay attention that in terms of realization this pattern is similar to the factory design pattern
"""

import random
from enum import Enum

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')

class Tree(object):
    pool = dict()
    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj
    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({}, {})'.format(self.tree_type, age, x, y))

def main():
    rnd = random.Random()
    age_min, age_max = 1, 30
    min_point, max_point = 0, 100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max), 
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max), 
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max), 
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1
        
    print('trees rendered: {}'.format(tree_counter))
    print('tree actually created: {}'.format(len(Tree.pool)))

if __name__ == '__main__':
    main()
        

        
