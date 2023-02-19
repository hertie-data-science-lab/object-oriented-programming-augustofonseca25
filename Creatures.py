# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:49 2023

@author: Hannah
"""

from abc import ABCMeta
from random import random, randint


class Creature(metaclass=ABCMeta):

    def __init__(self):
        pass


    # def __init__(self, position):
    #     self.__position__ = position
    #     pass


    def move(self, actual_position, choices): # function to check what will be the decision about the movement. Returns the new position
        if choices == 0: # If the animal can only move down or stay
            if randint(0, 1) != 0: # if the decision is to  move
                return actual_position + 1  # based on the decision to move, return the new position
            else:  # if the decision is NOT to move
                return actual_position #returns the same position
        elif choices == 1: # If the animal can move up, down or stay
            move_decision = randint(0, 2)
            if move_decision == 0:  # if the decision is to stay
                return actual_position
            elif move_decision == 1: # if the decision is to move down
                return actual_position+1 # tries to go to the next position
            else: # if the decision is to move up
                return actual_position-1 # tries to go to the previous position
        else: # If the animal can only move up or stay
            if randint(0, 1) != 0: # If the decision is to move
                return actual_position -1 # returns the previous position
            else: # If the decision is NOT to move
                return actual_position  #returns the same position


class Bear(Creature):

    def __init__(self):
        super().__init__()
        self.title = 'bear'
        pass


class Fish(Creature):

    def __init__(self):
        super().__init__()
        self.title = 'fish'
        pass
