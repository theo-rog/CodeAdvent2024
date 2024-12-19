#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:30:00 2024

@author: theorogers
"""

import requests

# URL of the input
link = "https://adventofcode.com/2024/day/9/input"

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

response_decoded = []
index = 0

for n, digit in enumerate(response):
    if digit != "\n" and digit != "":
        if (-1)**n == 1:  # Not free space
            response_decoded.extend([index] * int(digit))
            index += 1
        else:  # Free space
            response_decoded.extend(["."] * int(digit))

#%% 1.2
len(response_decoded)


while "." in response_decoded:
    
    for i in range(len(response_decoded)-1, -1, -1):
        if response_decoded[i] == ".":
            response_decoded = response_decoded[:-1]
            
        elif response_decoded[i] != "." and "." in response_decoded[:i]:
            index = response_decoded.index(".")
            
            #response_is_sorted = True
            #for char in response_decoded[index:]:
            #    if char != ".":
            #        response_is_sorted = False
                    
          #  if response_is_sorted:
          #       break
          #       break
               
                
                
            
            response_decoded[index] = response_decoded[i]
            response_decoded[i] = "."
            response_decoded = response_decoded[:-1]
            #print(f"RD: {response_decoded}")
            break
    #response_is_sorted = True
    #for char in response_decoded[index:]:
    #    if char != ".":
    #        response_is_sorted = False
            
   # if response_is_sorted:
    #     break
        
#%% 1.3

checksum = 0

for j, dig in enumerate(response_decoded):
    checksum += j * dig

#Ans = 6259790630969    

#%%Problem 2   

 
        
        