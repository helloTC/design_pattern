#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'''
 Abstract factory
 A game for children or adults
 chosen by their age
'''

# Game for children
class Frog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def interact_with(self, obstacle):
        print('{} the Frog enconters {} and {}!'.format(self, obstacle, obstacle.action()))
   
class Bug:
    def __str__(self):
        return 'A bug'
    def action(self):
        return 'eats it'

class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return '\n\n\t-------- Frog World --------'
    def make_character(self):
        return Frog(self.player_name)
    def make_obstacle(self):
        return Bug()

# Game for adults
class Wizard:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(self, obstacle, obstacle.action()))

class Ork:
    def __str__(self):
        return 'an evil ork'
    def action(self):
        return 'kills it'

class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name
    def __str__(self):
        return '\n\n\t-------------Wizard World----------------'
    def make_character(self):
        return Wizard(self.player_name)
    def make_obstacle(self):
        return Ork()

class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()
    def play(self):
        self.hero.interact_with(self.obstacle)

def validate_age(name):
    try:
        age = input('welcome {}. How old are you?'.format(name))
    except ValueError as err:
        print("Age {} is invalid, please try again..".format(age))
        return (False, age)
    return (True, age)

def main():
    name = input("Hello. What's your name?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()

if __name__ == '__main__':
    main()



