#!/usr/bin/env python3
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
link = "https://adventofcode.com/2024/day/2/input"

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

reports = response.split("\n")


safe_count = 0

for report in reports :
    safe = True # Assume that the report is safe
    
    if report != "": # Skip empty reports
    
        report = report.split(" ")
        
        # Create new list of integers
        report_int = [] 
        for i in range(len(report)): 
             report_int.append(int(report[i]))
             
        # Only work on reports that are longer than 2
        if len(report_int) > 1:
            
            # Operate on lists that indicate the sequence is strictly increasing/decreasing by first two terms
            # If the sequence is strictly increasing/decreasing then the first two terms will be too
            
            if report_int[0] > report_int[1]: # Strictly decreasing check 
                # Check every distance (there are (len - 1) distances)
                for i in range(len(report_int)-1):
                    dist = report_int[i] - report_int[i+1]
                    
                    if dist > 3 or dist < 1: # Unsafe distances
                        safe = False
                        
            elif report_int[0] < report_int[1]: # Strictly increasing check
                for i in range(len(report_int)-1):
                    dist = report_int[i+1] - report_int[i]
                    if dist > 3 or dist < 1:
                        safe = False    
            else: # If the first two elements are the same, then it is unsafe
                safe = False
    else: safe = False
    
    # Counting Function
    if safe:    
        safe_count+=1

print(safe_count)

#ans = 311

#%% Problem 2

safe_count = 0

# Much similar to before
for report in reports :
    safe_option = False
    if report != "":
        report = report.split(" ")
        report_int = []
        for i in range(len(report)):
             report_int.append(int(report[i]))
             
        if len(report_int) > 1:
            
            safe_option = False # Here we assume that there is not a safe possibility 
            
            # Every sequence with the j^th element removed is checked to see if it is safe
            for j in range(len(report_int)):
                j_safe = True # Assume that every option is safe
                
                # Removing the j^th element to create new list
                report_int_2 = report_int[:j] + report_int[j + 1:] 
            
                # If the new sequence fails the same checks as before then it is deemed unsafe
                if report_int_2[0] > report_int_2[1]: # Decreasing
                    for i in range(len(report_int_2)-1):
                        dist = report_int_2[i] - report_int_2[i+1]
                        if dist > 3 or dist < 1:
                            j_safe = False
                            
                            
                elif report_int_2[0] < report_int_2[1]: # Increasing
                    for i in range(len(report_int_2)-1):
                        dist = report_int_2[i+1] - report_int_2[i]
                        if dist > 3 or dist < 1:
                            j_safe = False
                else:
                    j_safe = False
                
                # If there is a safe possibility then the sequence will survive previous checks
                if j_safe:
                    safe_option = True
                    # The sequence is broken as further checks do not need to be completed
                    break
    
    if safe_option:
        
        safe_count+=1

print(safe_count)

# ans = 386


            
            