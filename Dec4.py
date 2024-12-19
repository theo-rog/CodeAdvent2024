# -*- coding: utf-8 -*-
"""
Created on Mon Dec 4 15:01:39 2024

@author: theorogers
"""



import requests

# URL of the input
link = "https://adventofcode.com/2024/day/4/input"

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

# Split the grid into a list of lists for easier processing
rows = response.split("\n")
grid = [list(row) for row in rows if row !='']

count = 0

# Create a string to iterate through
XMAS = "XMAS"

# Search the grid for "X"
for j in range(len(grid)):
    for i in range(len(grid[j])): # I think i and j are in the wrong place, notation wise, but its not deep
        
        if grid[j][i] == "X":
            
            # Search every legal direction from (j,i) 
            for i_factor in (-1,0,1):
                for j_factor in (-1,-0,1):
                        
                    # Check if the string follows
                    for k, character in enumerate(XMAS):
        
                        if (len(grid) > i_factor*k + i  >= 0) and (len(grid) > j_factor*k + j >= 0):
                            
                            # If for a direction the string does not follow, then break and try a new direction/entry
                            if grid[j+j_factor*k][i+i_factor*k] != character:
                                break
                            
                            # If the string is complete, then count this
                            elif k ==3 :
                                count+=1
                
print(count)

# Ans = 2514
             
#%% Problem 2

count = 0

# Search the grid again
for j in range(len(grid)):
    for i in range(len(grid[j])):
        
        # Start with an A
        if grid[j][i] == "A":
            
            # Only valid indices
            if (len(grid)-1 > i  > 0) and (len(grid)-1 >  j > 0):
                # Create placeholder variables for the left to right, 3 length, diagonal string, around "A"
                LR = grid[j-1][i-1] + grid[j][i] + grid[j+1][i+1] 
                # Then the right to left
                RL = grid[j-1][i+1] + grid[j][i] + grid[j+1][i-1]
                
                # If they satisfy the necessary requirements...
                LR_true = LR == "MAS" or LR =="SAM"
                RL_true = RL == "MAS" or RL =="SAM"
                
                #... then it counts
                if LR_true and RL_true:
                    count+=1
            

print(count)
                
                