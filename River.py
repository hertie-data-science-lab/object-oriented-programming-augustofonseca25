# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Hannah
"""
import numpy as np

#from Creatures import Creature, Bear, Fish
from Creatures import *
from random import random, randint


class River:
    
    def __init__(self, n_room):

        self.__n_room = n_room
        self.list_species = np.random.choice([Bear(), Fish(), None], self.__n_room).tolist()

    def __get_animal_specie__(self, position): # gets an element at a specific position in the river
        '''Return the animal specie in a specific position in the river'''
        return self.list_species[position]

    def __set_animal_specie__(self, position, specie): # changes an element in the river
        '''Set the animal specie in a specific position in the river'''
        self.list_species[position] = specie


    def display(self):
        print("===================")
        print("Ecosystem status:\n")
        print(self.list_species, sep = "\n")
        print("===================")

    # Method to count using lists
    def count_none_positions(self): #Counts the number of empty spots
        return self.list_species.count(None)
    def count_fish_elements(self): #Counts the number of empty spots
        return self.list_species.count(Fish)

    def random_empty_spot(self): #Returns an empty spot randomly
        possible_spots = []
        for key in range(self.__n_room-1): #Checks each element of the river
            if self.list_species[key] == None:
                possible_spots.append(key)  # Appends the position of each empty spot
        return random.choice(possible_spots)

    def movements(self): # Calls the animals to check if they intend to move

        if self.count_none_positions() != 0 or self.count_fish_elements() != 0: # Check if there is an empty spot and if there
            river_pos_choice = randint(0, self.__n_room-1) # Define which animal will try to move
            # Call the creature`s method to decide if the animal will move or not. Receive the expected new position
            if river_pos_choice == 0: # If it`s the 1st element
                a = self.__get_animal_specie__(river_pos_choice) # Check the animal in the target position
                new_position = a.move(river_pos_choice, 0) # Get the new intended position from method move (class Creatures)
            elif river_pos_choice == self.__n_room-1:  # If it`s the last element
                a = self.__get_animal_specie__(river_pos_choice) # Check the animal in the target position
                new_position = a.move(river_pos_choice, 2) # Get the new intended position from method move (class Creatures)
            else:  # If it`s an intermediary element
                a = self.__get_animal_specie__(river_pos_choice)# Check the animal in the target position
                new_position = a.move(river_pos_choice, 1) # Get the new intended position from method move (class Creatures)
            # Call the method to define the conflicts between the animals and effectivelly move them
            self.define_conflicts(river_pos_choice, new_position)

    '''
    Based on the output of the method movement, the next method "define_conflicts" evaluate 
    which animal will survive and move in each case. It`s the function that effectively move the animals.
    '''
    def define_conflicts(self, actual_position, new_position):

        animal_to_move = self.__get_animal_specie__(actual_position) # Check what`s the animal which will move
        new_position_content = self.__get_animal_specie__(new_position) # Check what`s the content of the intended position.

        if new_position_content == None: # if the position is empty
            self.__set_animal_specie__(new_position, animal_to_move) # move the animal to the new position
            self.__set_animal_specie__(actual_position, None) #Change the old position to empty
        elif new_position_content == Bear(): # If the new position is occupied by a bear
            if animal_to_move == Fish(): # If the animal that wants to move is a fish
                self.__set_animal_specie__(actual_position, None)  # The fish dies. Set the position to empty
            elif animal_to_move == Bear() and self.count_none_positions != 0: # If the animal that wants to move is also a bear and there is an empty spot
                self.__set_animal_specie__(self.random_empty_spot, animal_to_move) # Assign a new animal to an empty spot
        elif new_position_content == Fish():  # If the new position is occupied by a fish
            if animal_to_move == Bear(): # If the animal that wants to move is a bear
                self.__set_animal_specie__(new_position, animal_to_move)  # The fish dies. The bear moves to the new position
                self.__set_animal_specie__(actual_position, None)  # Change the bear`s old position to empty
            elif animal_to_move == Fish() and self.count_none_positions != 0: # If the animal that wants to move is also a fish and there is an empty spot
                self.__set_animal_specie__(self.random_empty_spot, animal_to_move)  # Assign a new animal to an empty spot




