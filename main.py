# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:05:41 2023

@author: Hannah
"""
import time
import random

from River import River

river = River(10) # create the object river - length 10
#river.initialize()
river.display() # display the elements randomly allocated


timer_interval = 10 # an interval to rerun the animals movements

'''
This while control the repeated execution of the movement loop.
It will stop only if there is no empty spots AND if there is no fishes.
I made this way because I understood the bears will eat all fishes in the river.
'''
while river.count_none_positions() != 0 or river.count_fish_elements() !=0:
    river.movements() # call the function to move one animal randomly assigned
    river.display() # show us the partial result
    time.sleep(timer_interval) # interval to run again