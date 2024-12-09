# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:01:39 2024

@author: theorogers
"""



import requests

# URL of the input
link = "https://adventofcode.com/2024/day/5/input"

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

# Splitting the response and rules
response_split = response.split("\n\n")
rules = response_split[0].split("\n")
updates = response_split[1].split("\n")

#Formatting the updates as a list of lists
update_list = []
for update in updates:
    if update != '':
        pages = update.split(",")
        page_list = []
        for page in pages:
            
            page_list.append(int(page))
        update_list.append(page_list)

# A function to check if a given rule is followed in a series
def index_check(X,Y,series):
    if X in series and Y in series:

        if series.index(X) > series.index(Y):
            return False
        else:
            return True
    else:
        return True

# Formatting X|Y pairs as lists
XY_list = []            
for rule in rules:
    pair = []
    XY = rule.split("|")
    pair.append(int(XY[0]))
    pair.append(int(XY[1]))

    XY_list.append(pair)

# Creating a list of incorrect lists
wrong_list =[]

count = 0
for update in update_list:
    pass_check = True # Assume that the list passes, until proven otherwise
    for XY in XY_list:
        if index_check(XY[0],XY[1],update):
            pass
        else: # If the series does not pass the check then it has failed
            pass_check = False
            break
    
    # If it passes the check then the middle value is added
    if pass_check == True:
        len_update = len(update)
        middle_index = int((len_update)/2)
 
        count+= int(update[middle_index])
    else:
        wrong_list.append(update)
        
print(count)
            
# 6251 < Ans < 13134

#%% Problem 2

# Define a function to swap two items in a list
def swap_item(X,Y,series):
    if X in series and Y in series:
        X_index = series.index(X)
        Y_index = series.index(Y)       
        series[X_index], series[Y_index] = series[Y_index], series[X_index]
        return(series)
 
# Iterate through the incorrect updates
count = 0
for update in wrong_list:
    unsorted = True
    
    while unsorted == True: # Check if the series satisfies the rules after swaps
        
        for XY in XY_list: # Swapping items if they do not satisfy the criteria
            update_len = len(update)
            if index_check(XY[0],XY[1],update):
                pass
            else:
                series = swap_item(XY[0], XY[1], update)
                
        # Checking if they pass for every value (similar to before)
        pass_check = True
        for XY in XY_list:
            if index_check(XY[0],XY[1],update):
                pass
            else:
                pass_check = False
                break
            
        if pass_check == True:
            len_update = len(update)
            middle_index = int((len_update)/2)
            count+= int(update[middle_index])
            unsorted = False


# Ans = 6897

