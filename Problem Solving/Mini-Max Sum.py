#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    
    max = 0
    min = 0
    
    for i in range(len(arr) - 1):
        min += arr[i]
        
    for i in range(len(arr) - 1, 0, -1):
        max += arr[i]
        
    print(min, max)
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
