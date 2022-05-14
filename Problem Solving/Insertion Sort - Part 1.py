#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    tmp = arr[n - 1]
    b = sorted(arr)

    for i in range(n - 1, 0, -1):
        a = False
        if(arr[i - 1] > tmp):
            arr[i] = arr[i - 1]
            a = True
        
        elif(arr[i - 1] < tmp and not(tmp in arr)):
            a = True
            arr[i] = tmp
        
        if(a):
            for i in arr:
                print(i, end = ' ')
            print()
    
    if(arr != b):
        for i in b:
            print(i, end = ' ')
        print()

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
