#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def funnyString(s):
    # Write your code here
    r = reversed(s)
    ascii_s = [ord(x) for x in s]
    ascii_r = [ord(x) for x in r]
    diff_s = [abs(y-x) for x, y in zip(ascii_s[0::], ascii_s[1::])]
    diff_r = [abs(y-x) for x, y in zip(ascii_r[0::], ascii_r[1::])]
    if diff_s == diff_r:
        return "Funny"
    else:
        return "Not Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
