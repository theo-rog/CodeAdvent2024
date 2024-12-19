#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:39:33 2024

@author: theorogers
"""

import requests

# URL of the input
link = "https://adventofcode.com/2024/day/10/input"

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



def check_surroundings(i,j,grid):
    coords = []
    end = False

    if int(grid[i][j]) != 9:
        for k in (0,1,-1):
            for l in (1,-1,0):
                if not (k!= 0 and l!= 0):
                    



                    if len(grid) > i+k >= 0 and len(grid[i]) > j+ l >= 0 :
                        if int(grid[i+k][j+l]) == (int(grid[i][j]) + 1):
                            coords.append((i+k,j+l))


                        
    elif int(grid[i][j]) == 9:
        end = True
        
    
    if coords != [] and end:
        return(coords,end)
    else:
        return(coords,end)
    
trail_number_count= 0

for i, row in enumerate(grid):
    for j, item in enumerate(row):
        if int(grid[i][j]) == 0:

            paths = 0 
            path_exists = True
            visited = set()
            coords_to_check = [(i,j)]
            while path_exists:
                

                for coord in coords_to_check:

                    if not coord in visited:
                        coords, end = check_surroundings(coord[0],coord[1],grid)
                        for coords_to_append in coords:
                            coords_to_check.append(coords_to_append)
                        

                        if end:
                            paths+= 1
                            path_exists = True

                            visited.add(coord)

                    visited.add(coord)
                    coords_to_check.remove(coord)


                        
                if not coords_to_check:
                        path_exists = False

            trail_number_count += paths 
print(trail_number_count)
# Ans = 517

#%% Problem 2



trail_number_count= 0

for i, row in enumerate(grid):
    for j, item in enumerate(row):
        if int(grid[i][j]) == 0:

            paths = 0 
            path_exists = True
            coords_to_check = [(i,j)]
            while path_exists:
                

                for coord in coords_to_check:


                    coords, end = check_surroundings(coord[0],coord[1],grid)
                    for coords_to_append in coords:
                        coords_to_check.append(coords_to_append)
                    

                    if end:
                        paths+= 1
                        path_exists = True




                    coords_to_check.remove(coord)


                        
                if not coords_to_check:
                        path_exists = False

            trail_number_count += paths 
print(trail_number_count)
# Ans = 1116
