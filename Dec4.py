# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:01:39 2024

@author: theorogers
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:04:56 2024

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

rows = response.split("\n")
grid = [list(row) for row in rows if row !='']

count = 0
XMAS = "XMAS"

for j in range(len(grid)):
    for i in range(len(grid[j])):
        
        if grid[j][i] == "X":
            
            for i_factor in (-1,0,1):
                for j_factor in (-1,-0,1):
                        
                    for k, character in enumerate(XMAS):
                

                        if (len(grid) > i_factor*k + i  >= 0) and (len(grid) > j_factor*k + j >= 0):
                            
                            if grid[j+j_factor*k][i+i_factor*k] != character:
                                break
                            
                            elif k ==3 :
                                count+=1
                
print(count)

#ans < 3011
             
#%% Problem 2

count = 0
MAS = "MS"

for j in range(len(grid)):
    for i in range(len(grid[j])):
        
        if grid[j][i] == "A":
            if (len(grid)-1 > i  > 0) and (len(grid)-1 >  j > 0):
                LR = grid[j-1][i-1] + grid[j][i] + grid[j+1][i+1]
                RL = grid[j-1][i+1] + grid[j][i] + grid[j+1][i-1]
                LR_true = LR == "MAS" or LR =="SAM"
                RL_true = RL == "MAS" or RL =="SAM"
                if LR_true and RL_true:
                    count+=1
            

print(count)
                
                