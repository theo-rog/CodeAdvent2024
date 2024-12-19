#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 19:59:18 2024

@author: theorogers
"""


import requests

# URL of the input
link = "https://adventofcode.com/2024/day/6/input"

# My session cookie
session_cookie = "53616c7465645f5ffaebb67567bc62b228c1b4a9adbc22469d6e2c4090c16ec9d70c1b91bc7eeac3d4d58f8f4b7a0303cf58bc09be1b56e33f6933cf13615c50"

# Pass the session cookie as a dictionary
cookies = {
    'session': session_cookie
}

# Get request to fetch the input
response = requests.get(link, cookies=cookies)

response = response.content.decode('utf-8')
response = str(response)


#%% Problem 1

from copy import deepcopy

# Split response into a grid
rows = response.split("\n")
grid = [list(row) for row in rows if row !='']

import math

# Iterate through the grid to find the start position
for i,row in enumerate(grid):

    if "^" in row:
        start_i = i
        start_j = row.index("^")

# The initial angle from the start position (s.t. sin(\theta) + cos(\theta) = initial direction of travel)
# (In radians)
start_angle = -math.pi/2

prob_1_grid = deepcopy(grid)  # Create a clean copy of the grid for problem 1

# A function to run the simulation
def run_sim(start_angle, start_i, start_j, prob_grid, problem):

    n = 0 
    on_map = True
    start = True     
    grid = prob_grid
    
    # Set 9999 as a limit for number of iterations
    while on_map and n < 9999:
        
        # This is how much the rotation amount changes each time
        rotation_amount = math.pi/2
        
        # Starting values
        if start:
            position_i = start_i
            position_j = start_j
            angle = start_angle
            start = False
        
        # The position at iteration "n" is marked as visited
        grid[position_i][position_j] = "X"
       
        # New positions are updated using trig
        new_i = position_i + int(math.sin(angle))
        new_j = position_j + int(math.cos(angle))
        
        # Check if on the map, if not, break
        if new_i >= len(grid) or new_i < 0 or new_j >= len(grid[start_i]) or new_j < 0:
            on_map = False
    
            break
            
        # Check next grid position
        grid_character = grid[new_i][new_j]
        
        # If valid, update the position
        if grid_character == "." or grid_character == "X" or grid_character == "^":
    
            position_i = new_i
            position_j = new_j
    
        # If valid, rotate the direction of travel
        if grid_character == "#":
            angle+= rotation_amount
            
        n+=1
    
    # Specific requirements for the first problem
    if problem == 1:    
        count_plus = 0
        for row in grid: # Count the visited lcoations
            row_count = row.count("X")
            count_plus += row_count
        print(count_plus)
    
    if problem == 2:
        return(n) # Count the number of iterations

# Run the sim
run_sim(start_angle, start_i, start_j, prob_1_grid, 1)

#Ans = 4982

#%% Problem 2

# The same but seeing how adding a barrier at each location impacts the simulation, for every coordinate:
count=0
for i, row in enumerate(prob_1_grid):
    for j, item in enumerate(row):

        new_grid = deepcopy(grid)
        new_grid[i][j] = "#"

        n = run_sim(start_angle, start_i, start_j, new_grid, 2)

        if n == 9999:
            count+= 1

    
print(count)

# Ans = 1663


            
            