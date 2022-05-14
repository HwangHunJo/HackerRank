#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    global m
    global n
    
    num_apple = 0
    num_orange = 0
    
    apple_loc = [0]*m
    orange_loc = [0]*n
    
    for i in range(m):
        apple_loc[i] = a + apples[i]
    
    for i in range(n):
        orange_loc[i] = b + oranges[i]
        
    
    for i in apple_loc:
        if(i >= s and i <= t):
            num_apple += 1
    
    for i in orange_loc:
        if(i >= s and i <= t):
            num_orange += 1
            
    print(num_apple)
    print(num_orange)
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
