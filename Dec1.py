#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:04:56 2024

@author: theorogers
"""

import requests

# URL of the input
link = "https://adventofcode.com/2024/day/1/input"

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

# Create 2 empty lists
list_1 = []
list_2 = []

# Split the input into rows
rows = response.split("\n")
for row in rows:
    # Only work on non-empty rows
    if row != '':
        # Split rows by which list
        row = row.split("   ")
        # Append items to correct list
        if row[0]:
            list_1_item = int(row[0])
            list_1.append(list_1_item)
        if row[1]:
            list_2_item = int(row[1])
            list_2.append(list_2_item)
    
    
    
# Sort the lists 
list_1.sort()
list_2.sort()

# Calculate the total distances
total_dist = 0
for i in range(len(list_1)):
    dist = abs(list_1[i] - list_2[i])
    total_dist+=dist
    
#Ans = 2285373


#%% Cell 2

# Calculate similarity score by multiplying theinstances of each item in list 1, by its frequency in list 2
sim_score = 0 
for j in list_1:
    count_j = j * list_2.count(j)
    sim_score+=count_j
    
#Ans = 21142653
    
    
    
    