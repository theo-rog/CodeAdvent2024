#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 20:58:06 2024

@author: theorogers
"""

import requests

# URL of the input
link = "https://adventofcode.com/2024/day/8/input"

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

rows = response.split("\n")
grid = [list(row) for row in rows if row !='']

import string

# Create a set of all upper and lowercase characters
chars = set(string.ascii_lowercase + string.ascii_uppercase+"1234567890")

antinodes = []
for char in chars:
    found_chars = []
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if grid[i][j] == char:
                found_chars.append((i,j))
                
    for k, coords in enumerate(found_chars):
        if k!= len(found_chars):
            for coords2 in found_chars[k+1:]:
                i_distance = coords[0] - coords2[0]
                j_distance =  coords[1] - coords2[1]

                
                antinode_1 = (coords[0] + i_distance, coords[1] + j_distance)

                antinode_2 = (coords2[0] - i_distance, coords2[1] - j_distance)

                if i_distance != 0 and j_distance != 0:
                    if not antinode_1 in antinodes and len(grid) > antinode_1[0] >= 0 and len(row) > antinode_1[1] >= 0:
                        antinodes.append(antinode_1)
                    
                            
                    if not antinode_2 in antinodes and len(grid) > antinode_2[0] >= 0 and len(row) > antinode_2[1] >= 0:
                        antinodes.append(antinode_2)
                    

               

# Ans = 247

#%% Problem 2

antinodes = []
for char in chars:
    found_chars = []
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if grid[i][j] == char:
                found_chars.append((i,j))
                
    for k, coords in enumerate(found_chars):
        if k!= len(found_chars):
            for coords2 in found_chars[k+1:]:
                i_distance = coords[0] - coords2[0]
                j_distance =  coords[1] - coords2[1]
                
                if i_distance != 0 and j_distance != 0:
                    
                    for m in range(0,50):
    
                        antinode_1 = (coords[0] + m * i_distance, coords[1] + m* j_distance)
                        if len(grid) > antinode_1[0] >= 0 and len(row) > antinode_1[1] >= 0:
                            if not antinode_1 in antinodes:
                                antinodes.append(antinode_1)
                        else:
                            break
                            
                            
                    
                                
                    for m in range(0,50):
                        
                         antinode_2 = (coords2[0] - m * i_distance, coords2[1] - m * j_distance)
                         if len(grid) > antinode_2[0] >= 0 and len(row) > antinode_2[1] >= 0:
                             if not antinode_2 in antinodes:
                                 print(antinode_2)
                                 antinodes.append(antinode_2) 
                         else:
                            break


# 773 < Ans < 1638                   
                        
                


                


