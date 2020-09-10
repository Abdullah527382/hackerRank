#!/bin/python3

import math
import os
import random
import re
import sys

''' 
    Print a single integer denoting the number of letter of a's
    in the first n letters of the sinfinite string created by repeating s
    infinite amount of times
'''

# Complete the repeatedString function below.

def repeatedString(s, n):
    '''
    # Special case, if string is 1 lettered
    if (len(s) == 1):
        return n
    readString = ''
    charCount = 0
    i = 0
    while (i < n):
        if (charCount == len(s)):
            charCount = 0
        readString += s[charCount]
        # print(readString[charCount])
        charCount+=1
        i += 1
    return readString.count("a")
'''
    print (s[:n % len(s)])
    ''' 
    s.count("a") * (n // len(s)) calculates 'a' count of string char repetitions till n
    e.g. | s = aba, n = 10 | --> 2 * 10/3 = 6 
    then s[:n % len(s)].count("a") calculates remainder chars count right before n
    e.g. | s = aba, n = 10 | --> s[:10%3] -> s[:1].count("a") -> 1
    Note: [:n] takes the n first values in array s
    '''
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")



if __name__ == '__main__':

    
    s, n = input().strip(), int(input().strip())
    result = repeatedString(s, n)

    print(result)
