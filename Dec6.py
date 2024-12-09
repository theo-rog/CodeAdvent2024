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
rows = response.split("\n")
grid = [list(row) for row in rows if row !='']
import math

n=0
for i,row in enumerate(grid):

    if "^" in row:
        start_i = i
        start_j = row.index("^")
    
start_angle = -math.pi/2

prob_1_grid = deepcopy(grid)  # Create a clean copy of the grid for problem 1




start_angle = -math.pi/2

def run_sim(start_angle, start_i, start_j, prob_grid, problem):

    n = 0 
    on_map = True
    start = True     
    grid = prob_grid
         
    while on_map and n < 9999:
        
        rotation_amount = math.pi/2
        
        if start:
            position_i = start_i
            position_j = start_j
            angle = start_angle
            start = False
    
        grid[position_i][position_j] = "X"
       
        new_i = position_i + int(math.sin(angle))
        #print(f"{n}: new i : {new_i}, position_i: {position_i} +fac: { int( math.sin(angle) ) }")
    
        new_j = position_j + int(math.cos(angle))
        
        if new_i >= len(grid) or new_i < 0 or new_j >= len(grid[start_i]) or new_j < 0:
            on_map = False
    
            break
            
        grid_character = grid[new_i][new_j]
        
        if grid_character == "." or grid_character == "X" or grid_character == "^":
    
    
            position_i = new_i
            #print(f" new i : {new_i}, position_i: {position_i}")
    
            position_j = new_j
    
        
        if grid_character == "#":
            angle+= rotation_amount
            
    
    
        n+=1
    if problem == 1:    
        count_plus = 0
        for row in grid:
            row_count = row.count("X")
            count_plus += row_count
        print(count_plus)
    
    if problem == 2:

        return(n)

        
run_sim(start_angle, start_i, start_j, prob_1_grid, 1)

#Ans = 4982

#%% Problem 2

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


            
            