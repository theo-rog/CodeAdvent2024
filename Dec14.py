#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 22:06:45 2024

@author: theorogers
"""
import requests

# URL of the input
link = "https://adventofcode.com/2024/day/14/input"

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
import re
import math
robots = response.split("\n")
robots.pop(500)



def extract_pv(robot):
    pattern = r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)"  # Matches pos, vel
    match = re.search(pattern, robot)
    if match:
        p_x, p_y, v_x, v_y = map(int, match.groups())
        return {
            "p_x": p_x,
            "p_y": p_y,
            "v_x": v_x,
            "v_y": v_y,
        }

robots = [extract_pv(robot) for robot in robots]

seconds = 100

room_x = 101
room_y = 103

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for robot in robots:
    pos_x = (robot["p_x"] + (seconds * robot["v_x"]))%room_x
    pos_y = (robot["p_y"] + (seconds * robot["v_y"]))%room_y
    if pos_x == math.floor(room_x / 2) or pos_y == math.floor(room_y / 2) :
        pass
    elif pos_x < math.floor(room_x / 2):
        if pos_y < math.floor(room_y / 2):
            q1 += 1
        else:
           q2 += 1
    else:
        if pos_y < math.floor(room_y / 2):
            q3 += 1
        else:
            q4 += 1
        
safety_score = math.prod(quadrant for quadrant in (q1, q2, q3, q4))
print(safety_score)

#Ans = 230461440

#%% Problem 2

def return_grid(robots, room_x, room_y,display = False):
    grid = [['.' for _ in range(room_x)] for _ in range(room_y)]
    for robot in robots:
        grid[robot["p_y"]][robot["p_x"]] = '#'
    
    if not display:
        return(grid)
    else:
        for row in grid:
            print(''.join(row))
        print("\n")
    

def has_continuous_hashes(row, n):
    count = 0
    for cell in row:
        if cell == '#':
            count += 1
            if count >= n: 
                return True
        else:
            count = 0  
    return False

grid = return_grid(robots, room_x, room_y)


end= False

for t in range(room_x * room_y):
    seconds = t+1
    visited_states = set()
    


    
    for n, robot in enumerate(robots):
        robot["p_x"] +=  robot["v_x"]
        robot["p_x"] = robot["p_x"] % room_x
        
        robot["p_y"] +=  robot["v_y"]
        robot["p_y"] = robot["p_y"] % room_y
        
        
        visited_states.add((robot["p_x"],robot["p_y"]))
        
    if len(visited_states) == len(robots):
        print(seconds)
            
    grid = return_grid(robots, room_x, room_y)
    for i, row in enumerate(grid):
        if has_continuous_hashes(row, 6):
                #print(seconds)
                if seconds == 6668:
                    grid = return_grid(robots, room_x, room_y,True)

                    



# Ans = 6668