#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:13:02 2024

@author: theorogers
"""

import requests

# URL of the input
link = "https://adventofcode.com/2024/day/13/input"

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
import numpy as np

tokens = 0

response_split = response.split("\n\n")

# Extracting each number from the input:
def extract_numbers(game):

    pattern = (
        r"Button A: X\+(\d+), Y\+(\d+)\n"      # Matches Button A's X and Y values
        r"Button B: X\+(\d+), Y\+(\d+)\n"      # Matches Button B's X and Y values
        r"Prize: X=(\d+), Y=(\d+)"             # Matches Prize's X and Y values
    )
    
    match = re.search(pattern, game)
    if match:
        a_x, a_y, b_x, b_y, prize_x, prize_y = map(int, match.groups())
        return {
            "a_x": a_x,
            "a_y": a_y,
            "b_x": b_x,
            "b_y": b_y,
            "prize_x": prize_x,
            "prize_y": prize_y
        }

# Check statement for each solution
def check_ab(a,b):
    if a%1==0 and a>=0 and a<100 and b%1==0 and b>=0 and b<100:
        return(True)
    else:
        return(False)
        
# Processing the games
games = [extract_numbers(game) for game in response_split]

# Iterate through games
for game in games:
    
    # Represent the problem as two linear simultaneous equations
    button_combo = np.array([[game["a_x"], game["b_x"]], [game["a_y"], game["b_y"]]])  
    prizes = np.array([game["prize_x"],game["prize_y"]])
    
    # If the determinant of the matrix of coefficients is 0 then there is a single solution 
    if np.linalg.det(button_combo) != 0:
        
        # Solve
        sol = np.linalg.solve(button_combo,prizes)
        a = round(sol[0],9) # solutions require rounding as the solving of the system of equations sometimes produces results that are
                            # near but not exactly integers
        b = round(sol[1],9)
        
        # If the solution is valid, then add appropriate number of tokens
        if check_ab(a,b):
            tokens += 3*a + b


        
    # Otherwise check if there are infinte or no solutions (this case isn't applicable in this problem setting)
    else:
        print("no sol or inf sol")
        rank = np.linalg.matrix_rank(button_combo)
        if rank == 1: 
            print('inf sol')
            
tokens = int(tokens)
print(tokens)

# ans = 29438

#%% Problem 2

# This is the same but 10000000000000 is added to each prize location
tokens=0

def check_ab(a,b):
    if a%1==0 and a>=0 and b%1==0 and b>=0: # remove the constraint that a,b <100
        return(True)
    else:
        return(False)
        

games = [extract_numbers(game) for game in response_split]

for game in games:
    button_combo = np.array([[game["a_x"], game["b_x"]], [game["a_y"], game["b_y"]]])  
    prizes = np.array([game["prize_x"]+10000000000000,game["prize_y"]+10000000000000])
    

    
    if np.linalg.det(button_combo) != 0:
        sol = np.linalg.solve(button_combo,prizes)
        a = round(sol[0],4) # Errors are worse as prize locations increase, so rounding needs to be less constrained 
        b = round(sol[1],4)
    
        if check_ab(a,b):
            tokens += 3*a + b

        
    
    else:
        print("no sol or inf sol")
        rank = np.linalg.matrix_rank(button_combo)
        if rank == 1: 
            print('inf sol')
            
tokens = int(tokens)
print(tokens)

#71154919667297 

#104958599303720
        