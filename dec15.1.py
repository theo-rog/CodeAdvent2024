#%% Intro bits

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 00:32:40 2024

@author: theorogers
"""

import requests

# URL of the input
link = "https://adventofcode.com/2024/day/15/input"

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



#%%Problem 1

import re 

def vector_add(vector_1,vector_2): # Define an adding vector function
    vector_3 = (vector_2[0] + vector_1[0],vector_2[1] + vector_1[1])
    return(vector_3)

instructions_grid = response.split("\n\n") # Split the grid into processable format
grid, instructions = instructions_grid

instructions = re.sub(re.escape("\n"), "", instructions) 

grid = grid.split("\n")
grid = [list(row) for row in grid] # Format grid as list of lists

inst_to_dire = { # Dictionary that converts instructions to co-ordinate directions
    ">": ((0,1)),
    "<": ((0,-1)),
    "^": ((-1,0)),
    "v": ((1,0)),
    "\n": ((0,0))
    }
    
for i, row in enumerate(grid): # finding the start point
    if "@" in row:
        start_i = i
        start_j = row.index("@")
        
def check_ahead(series): # A function that checks what to expect ahead in a series
    if "#" in series:
        wall_index = series.index("#")
    
    series = series[:wall_index]

    new_series = [] # A list of what to expect ahead
    
    for n, item in enumerate(series):
        #print(f"n: {n}")
        
        if item == "@": # If its the start, then the @ is moving
            moving_char = "@"
            
        elif item == "#": # If a hash is encountered, then nothing happens
         # (only occurs after @, as "."s and " O" with "#"'s ahead result in function breaking)
            new_series.append(moving_char) # (just a "@")
            break
        
        elif item == ".": # If a dot occurs then the moving character moves ahead and the loop stops
        
            if moving_char == "@": # If the robot moves, it leaves an empty space behind
                new_series.append(".")
            new_series.append(moving_char)   

            break
        
        elif item == "O": # If the robot encounters a box, the moving character changes
            
            if "." in series[n:]:
                if moving_char == "@":
                    new_series.append(".")
                new_series.append(moving_char)   
                    
                moving_char = item
                
            else:
                break
            
            
        #print(f"mov char: {moving_char}")
        #print(new_series)
        
    return(new_series)

robo_position = (start_i,start_j) # initialise position
start= True

count = 0

uhohs = set()

#instructions = ">>>>>>>>>"
for instruction in instructions:
    
    #print(instruction)
    count += 1
    #print(f"count: {count}")

    if start:
        position = robo_position
        start = False
        
    direction = inst_to_dire[instruction]

    
    ahead = []
    
    pos_to_check = position
    
    for m in range(len(grid)):
        i,j  = pos_to_check
        
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
            ahead.append(grid[i][j])
            pos_to_check = vector_add(pos_to_check,direction)
        else:
            break

        
    #print(f"ahead: \n{ahead}\n")
    new_ahead = check_ahead(ahead)
    #print(new_ahead)
    
    pos_to_check = position
    
    #print(f"position1: {position}")
    for k in new_ahead:

        i_k, j_k = pos_to_check
        if k == "@":
            position = (i_k, j_k)
        grid[i_k][j_k] = k
        pos_to_check = vector_add(pos_to_check,direction)
    #print(f"position2: {position}")

score = 0


for i, row in enumerate(grid): 
    for j, item in enumerate(row): 
        if item == "O":
            score += (i*100) + j
            
#ans = 1318523

print(score)

#%% Problem 2

grid, instructions = instructions_grid

instructions = re.sub(re.escape("\n"), "", instructions) 

grid = grid.split("\n")
grid = [list(row) for row in grid] # Format grid as list of lists

new_grid = [[]]

for i, row in enumerate(grid): 
    new_row = []
    for j, item in enumerate(row): 
        if item == "@":
            new_row.append(item)
            new_row.append(".")
        elif item == "O":
            new_row.append("[")
            new_row.append("]")
        else:
           new_row.append(item)
           new_row.append(item)
    new_grid.append(new_row)
    
new_grid.pop(0)

def can_move(grid,direction,position):
    if direction == "<" or ">":
        ahead = []







def new_check_ahead(series,instruction): # A function that checks what to expect ahead in a series
    if "#" in series:
        wall_index = series.index("#")
    
    series = series[:wall_index]

    new_series = [] # A list of what to expect ahead
    
    for n, item in enumerate(series):
        #print(f"n: {n}")
        
        if item == "@": # If its the start, then the @ is moving
            moving_char = "@"
            
        elif item == "#": # If a hash is encountered, then nothing happens
         # (only occurs after @, as "."s and " O" with "#"'s ahead result in function breaking)
            new_series.append(moving_char) # (just a "@")
            break
        
        elif item == ".": # If a dot occurs then the moving character moves ahead and the loop stops
        
            if moving_char == "@": # If the robot moves, it leaves an empty space behind
                new_series.append(".")
            new_series.append(moving_char)   

            break
        
        elif item == "O": # If the robot encounters a box, the moving character changes
            
            if "." in series[n:]:
                if moving_char == "@":
                    new_series.append(".")
                new_series.append(moving_char)   
                    
                moving_char = item
                
            else:
                break
            
            
        #print(f"mov char: {moving_char}")
        #print(new_series)
        
    return(new_series)

