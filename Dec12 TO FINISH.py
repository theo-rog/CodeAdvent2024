#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:04:07 2024

@author: theorogers
"""

import requests

# URL of the input
link = "https://adventofcode.com/2024/day/12/input"

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
garden = [list(row) for row in rows if row !='']

assigned_plants = set()
cost = 0

plant_beds = []
for i, row in enumerate(garden):
    for j, plant in enumerate(row):
        # Every Plant
        if not (i,j) in assigned_plants:
            
            # Every non-assigned plant
            plant_bed = set()
            
            plant_bed.add((i,j))
            
            old_plant_bed_len = 0
            len_plant_bed = len(plant_bed) 
            
            # Finding the plant bed 
            while len_plant_bed > old_plant_bed_len:
                old_plant_bed_len = len(plant_bed)
                
                plants_to_add = set()
                for plant_of_bed in plant_bed:
                    i_new = plant_of_bed[0]
                    j_new = plant_of_bed[1]
                    
                    #Search around each plant in the plant bed
                    for k, l in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        if (len(garden) > i_new+k >= 0) and (len(row) > j_new+l >= 0) :   
                            if garden[i_new+k][j_new+l] == plant:
                                
                                plants_to_add.add((i_new+k,j_new+l))
                                assigned_plants.add((i_new,j_new))
                                
                
                for plant_of_bed in plants_to_add:
                    plant_bed.add(plant_of_bed)
                len_plant_bed = len(plant_bed)
            
            perim = 0
            
            plant_beds.append(plant_bed)
            for plant_in_bed in plant_bed:
                sides =0 
                i_new = plant_in_bed[0]
                j_new = plant_in_bed[1]
                for k, l in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    if (len(garden) > i_new+k >= 0) and (len(row) > j_new+l >= 0):   
                        if garden[i_new+k][j_new+l] != plant:
                            sides += 1
                    else:
                        sides += 1
                        
                            
                perim+=sides                
            cost += perim * len(plant_bed)

# Cost = 1449902 

#%% Problem 2

import math

def vector_sub(vector_1,vector_2):
    vector_3 = (vector_2[0] - vector_1[0],vector_2[1] - vector_1[1])
    return(vector_3)

def find_neighbours(plant,plant_bed):
    neighbours = []
    for k, l in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (i+k,j+l) in plant_bed:
            neighbours.append((i+k,j+l))
    return(neighbours)
    

plant_bed = plant_beds[0]
#def sides_count(plant_bed):
    

boundary_plants = []
for plant in plant_bed:
    i,j = plant
    for k, l in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if not ((i+k,j+l) in plant_bed):
            boundary_plants.append((i,j))
    
    
checked_plants = set()
start=True


while len(checked_plants) < len(boundary_plants):
    if start:
        tracing_plant = boundary_plants[0]
        sides = 1
        start = False
        old_plant = tracing_plant
    i,j = tracing_plant
    
    
    
    unchecked_neighbours = []
    for neighbour in find_neighbours(plant,plant_bed):
        if not neighbour in checked_plants:
            unchecked_neighbours.append(neighbour)
            
    ortho = False 
    if unchecked_neighbours:
        num_neighbours_dict = {
        unchecked_neighbour: len(find_neighbours(unchecked_neighbour, plant_bed))
        for unchecked_neighbour in unchecked_neighbours
    }  
    
    
    for unchecked_neighbour in unchecked_neighbours:
        
        if vector_sub(tracing_plant,old_plant) != vector_sub(neighbour,tracing_plant):
            tracing_plant = neighbour
            sides+=1
            ortho = True
            break
        
    if ortho == False:
        tracing_plant = neighbour
        
        
            
    
                


cost = 0
for plant_bed in plant_beds:
    print()
                
         
# 1820802 < 591108


