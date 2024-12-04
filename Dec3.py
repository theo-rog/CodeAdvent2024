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
link = "https://adventofcode.com/2024/day/3/input"

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

import re # To find the correct sequence

mul_sequence = r"mul\((\d{1,3}),(\d{1,3})\)" # The sequence to be found follows this regex
 
matches = re.findall(mul_sequence, response) # Find every instance of this

product_sum = 0

for matched in matches: # Multiply every match of digits found
    num1, num2 = matched
    num1 = int(num1)
    num2 = int(num2)

    product = num1*num2
    product_sum += product
    
print(product_sum)
#ans = 175700056

#%%Problem 2
    

# Split the response by "do()"s, so that every element starts as enabled
responses = response.split("do()")

# Removing everything in the responses that follows a "don't()" but comes before a "do()"
do_responses = [
    response.split("don't()")[0]
    for response in responses
] 

# Joining elemetns to create a string of valid instructions
do_responses = "".join(do_responses)

# As before
matches = re.findall(mul_sequence, do_responses)

product_sum = 0
    
for matched in matches:
    num1, num2 = matched
    num1 = int(num1)
    num2 = int(num2)

    product = num1*num2
    product_sum += product


print(product_sum)
# Ans = 71668682

