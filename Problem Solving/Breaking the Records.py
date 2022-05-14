#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    global n
    
    min = 1000
    max = 0
    
    cnt_min = 0
    cnt_max = 0
    for i in range(n):
        if(i == 0):
            min = scores[i]
            max = scores[i]
        else:
            if(min > scores[i]):
                min = scores[i]
                cnt_min += 1
            if(max < scores[i]):
                max = scores[i]
                cnt_max += 1
    return cnt_max, cnt_min
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
