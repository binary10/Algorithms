# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:08:38 2015

@author: Dan Kowalczyk

Programming in Java: An Interdisciplinary Approach
p. 154 - Problem 1.5.1
"""

maximum = None
minimum = None

while(True):
    stream_input = input()          # Next input from the stream
    if stream_input == '': break    # Do the loop until... Loop exit

    stream_input_int = int(stream_input)  

    # Initialize variables
    if maximum is None and minimum is None:
        maximum, minimum = stream_input_int, stream_input_int
    # Process subsequent values
    else:
        if stream_input_int > maximum:
            maximum = stream_input_int
    
        if stream_input_int < minimum:
            minimum = stream_input_int

print((minimum, maximum))