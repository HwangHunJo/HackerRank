#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    stat = s[8:10]
    s = s[0:8]
    hour, minute, second = map(int, s.split(":"))
    
    if(stat == "PM" and hour < 12):
        hour = hour + 12
        
    if(hour == 12 and stat == "AM"):
        hour = 0
        
    if(hour < 10):
        hour = '0' + str(hour)
    
    if(minute < 10):
        minute = '0' + str(minute)
    
    if(second < 10):
        second = '0' + str(second)
    
    return str(hour) + ":" + str(minute) + ":" + str(second)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
