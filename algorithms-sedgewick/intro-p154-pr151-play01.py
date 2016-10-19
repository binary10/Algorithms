# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:06:05 2015

@author: dankow01

This module defines a static class of ConsoleInput that produces
an input generator for use in foreach loops.
"""

class ConsoleInput:
    """
    This static class produces an input generator for use in 
    foreach loops.
    """    
    def Generator(self):
        """
        Outputs a generator that can be used to .
        """
        while(True):
            a = raw_input()
            if a == '': raise StopIteration
            yield a


def main():
    """
    Run the static method of ConsoleInput and loop inputs until blank.
    """
    c = ConsoleInput()
    in_gen = c.Generator() 
    for val in in_gen:
        print('You typed ' + str(val))
    

if __name__ == '__main__':
    main()

