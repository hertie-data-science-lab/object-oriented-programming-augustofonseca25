# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:05:41 2023

@author: Hannah
"""
import time
import random

from River import River

river = River(10)
#river.initialize()
river.display()

river.list_species[1].move(self,1,1)

timer_interval = 10

#random.randrange(0,2)

if river.count_none_positions() != 0 or river.count_fish_elements() !=0:
    river.movements()
    river.display()
    time.sleep(timer_interval)