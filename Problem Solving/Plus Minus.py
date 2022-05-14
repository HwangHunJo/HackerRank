#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    neg = 0
    pos = 0
    zero = 0
    div = len(arr)
    
    for i in arr:
        if(i < 0):
            neg += 1
        elif(i > 0):
            pos += 1
        else:
            zero += 1
    
    print("%.6f" %(pos/div))
    print("%.6f" %(neg/div))
    print("%.6f" %(zero/div))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
