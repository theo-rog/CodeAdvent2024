#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 15:36:50 2024

@author: theorogers
"""



import requests

# URL of the input
link = "https://adventofcode.com/2024/day/7/input"

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
import itertools

equations = response.split("\n")

def stringlist2intlist(series):
    series_list = []
    for string in series:
        if string != "":
            integer = int(string)
            series_list.append(integer)
    return(series_list)

count = 0

for equation in equations: 
    if equation != '':
        split = equation.split(":")
        ans = int(split[0])
        numbers = split[1].split(" ")
        numbers = stringlist2intlist(numbers)
        

        operation_poss_len = len(numbers)-1
        operations_poss = itertools.product(["+","*"], repeat = operation_poss_len)
        valid = False
        for operations in operations_poss:

            result = numbers[0]
            for i, op in enumerate(operations):
                if op == "+":
                    result += numbers[i+1]
                if op == "*":
                    result *= numbers[i+1]
                    
            if result == ans:
                valid = True
                break

            
        if valid == True:
            count+=ans
    
# Ans = 1399219271639

#%% Problem 2

def concatnum(a,b):
    a = str(a)
    b = str(b)
    c = a + b
    c = int(c)
    return(c)

count = 0

for equation in equations: 
    if equation != '':
        split = equation.split(":")
        ans = int(split[0])
        numbers = split[1].split(" ")
        numbers = stringlist2intlist(numbers)
        

        operation_poss_len = len(numbers)-1
        operations_poss = itertools.product(["+","*","||"], repeat = operation_poss_len)
        valid = False
        for operations in operations_poss:

            result = numbers[0]
            for i, op in enumerate(operations):
                if op == "+":
                    result += numbers[i+1]
                if op == "*":
                    result *= numbers[i+1]
                if op == "||":
                    result = concatnum(result,numbers[i+1])
                    
            if result == ans:
                valid = True
                break

            
        if valid == True:
            count+=ans

# Ans = 275791737999003 
                

        
        