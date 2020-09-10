
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    i = 0
    pairCount = 0
    countedNums = []
    while i < n:        
        if (ar[i] not in countedNums):
            if (ar.count(ar[i]) > 1):
                # print(ar[i])
                if (ar.count(ar[i]) % 2 == 0):
                    pairCount += int(ar.count(ar[i])/2)
                else:
                    pairCount += int(ar.count(ar[i])-1)/2
            countedNums.append(ar[i])
        # print(countedNums)
        i += 1
    return int(pairCount)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
