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
    # Write your code here
    hour, minute, second = s[:-2].split(":")
    is_pm = s[-2:] == "PM"
    if is_pm and int(hour) == 12:
        return s[:-2]
    elif is_pm and int(hour) != 12:
        return "{:0>2d}:{}:{}".format(int(hour)+12, minute, second)
    elif not(is_pm) and int(hour) == 12:
        return "{:0>2d}:{}:{}".format(int(hour)-12, minute, second)
    elif not(is_pm) and int(hour) != 12:
        return s[:-2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
