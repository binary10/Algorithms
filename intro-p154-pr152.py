# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:08:38 2015

@author: Dan Kowalczyk

Programming in Java: An Interdisciplinary Approach
p. 154 - Problem 1.5.2
"""

maximum     = None      # Maximum value encountered in the stream of data
minimum     = None      # Minimum value encountered in the stream of data
is_negative = None      # Property of last input -- used to restrict to postive

while(True):
    # Receive input
    if is_negative: stream_input = input('Please provide a positive int: ')  
    else: stream_input = input()          
    
    if stream_input == '': break        # Do the loop until... Loop exit
        
    # Evaluate the current input
    stream_input_int = int(stream_input)
    is_negative = stream_input_int < 0
    if (is_negative): continue          # Input is bad, get new input
    
    # If it's the first set of good inputs, initialize min and max
    if maximum is None and minimum is None:
        maximum, minimum = stream_input_int, stream_input_int
    # For all subsequent good inputs, set min and max accordingly
    else:
        if stream_input_int > maximum:
            maximum = stream_input_int
    
        if stream_input_int < minimum:
            minimum = stream_input_int

print((minimum, maximum))