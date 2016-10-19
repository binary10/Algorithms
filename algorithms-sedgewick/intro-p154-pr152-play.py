# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:51:34 2015

@author: dankow01

Testing the creation of generators.
Yield keyword to allow "send" value.
"""

def createGenerator():
    i = 0    
    while(True):
        out = i*i
        value = yield out                   # Set value to what is 'sent'
        if value is not None: i = value     # Check if something is sent
        else: i += 1
        if i > 10: raise StopIteration


g = createGenerator()
for i in g:
    print(i)
    if (i > 10000): break