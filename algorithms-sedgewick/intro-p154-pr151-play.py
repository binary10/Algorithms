# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 09:04:36 2015

@author: dankow01

This program demonstrates the concept of fenceposting.
The problem to solve is to do two actions, one of which must
always be the first and last. That action must also occur
at least once.
"""

def fencepost(posts):
    # Validate input
    valid_input = posts > 0
    
    # Proceed if valid
    if valid_input:
        while(True):                # Start infinite loop
            print('post')
            posts -= 1
            
            if posts == 0: break    # Loop exit: Stop when zero reached
                
            print('gap')

# This implementation fails at zero and duplicates code
def fencepost_for(posts):
    # Validate input
    for n in range(posts - 1):
        print('post')
        print('gap')
    print('post')



# Test client
import random

for n in range(10):
    print('This is loop ' + str(n))
    fencepost(random.randint(0,10))