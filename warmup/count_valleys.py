#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    currLevel = 0
    count = 0
    # iterate through the string 
    for char in s:
        if (char == 'D'):
            currLevel -= 1
        if (char == 'U'):
            currLevel += 1
            if (currLevel == 0):
                # print('Reached sea level from valley')
                count += 1
    return count
if __name__ == '__main__':

    n = int(input())

    s = input()
    
    result = countingValleys(n, s)

    print(result)
