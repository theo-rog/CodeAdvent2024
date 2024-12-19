#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:39:50 2024

@author: theorogers
"""

import requests

# URL of the input
link = "https://adventofcode.com/2024/day/11/input"

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

# From Dec7. I had issues importing directly
def stringlist2intlist(series):
    series_list = []
    for string in series:
        if string != "":
            integer = int(string)
            series_list.append(integer)
    return(series_list)

# Formatting every position as a list
stone_positions = response.split(" ")
stone_positions_list = stringlist2intlist(stone_positions)
stone_positions = [[stone] for stone in stone_positions_list]

# Function to calculate new number
def check_stone(stone_number):
    if stone_number != '':
        stone_number = int(stone_number)
        new_stone = []
        
        if stone_number == 0:
            new_stone.append(1)
        elif len(str(stone_number)) % 2 == 0:
            stone_number = str(stone_number)
            len_sn = int(len(stone_number)/2)

            new_num_1 = int(stone_number[:len_sn])
            new_num_2 = int(stone_number[len_sn:])
            new_stone.append(new_num_1)
            new_stone.append(new_num_2)
        else:
            new_stone.append(stone_number*2024)
        
        return(new_stone)

# A function to iterate through the positions and update each iterationg
def check_stone_list(stone_positions):
    new_stone_positions = []
    for stones in stone_positions:
        new_stone_numbers = []
        for stone in stones:
            checked_stones = check_stone(stone)
            for checked_stone in checked_stones:
                new_stone_numbers.append(checked_stone)
        new_stone_positions.append(new_stone_numbers)
                
    return(new_stone_positions)
                
                
times_to_blink = 25 

# Updating the list for every blink
for i in range(times_to_blink):
    stone_positions = check_stone_list(stone_positions)
    
# Counting the number of stones
num_stones = 0
for stone_position in stone_positions:
    num_stones += len(stone_position)
print(num_stones)
    
# Ans = 217812

#%% Problem 2

# Refactoring the problem to include dictionaries, one counting the number of stones in the system at the current state with
# each number (stones_count) and maps, which is used to map from one number to the numbers it creates. This makes the process 
# much more efficient

times_to_blink = 75

# New function to check the number of stones, using the maps
def check_stone_2(stone_number, maps):
    if stone_number in maps:
        return(maps[stone_number])
    else:
        new_stone_num = check_stone(stone_number)
        maps[stone_number] = new_stone_num
        return(new_stone_num)

# Setting an intial count fo each stone number
stones_count ={}
for stone in stone_positions_list:
    stones_count[stone] = stone_positions_list.count(stone)
    
maps = {}

# Iterating through blinks, and updating the counts of each stone
for blink in range(times_to_blink):
    new_stones_count = {}
    for stone in stones_count:
        new_nums = check_stone_2(stone, maps)
        for num in new_nums:
            if num in new_stones_count:
                new_stones_count[num] += stones_count[stone]
            else:
                new_stones_count[num] = stones_count[stone]
    stones_count = new_stones_count
    
# Counting the stones
num_stones = 0
for i in stones_count:
    num_stones += stones_count[i]
print(num_stones)    
    
# Ans = 259112729857522
        
    