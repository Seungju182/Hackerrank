#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase as lower

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def theLoveLetterMystery(s):
    # Write your code here
    center = len(s) // 2
    return sum(abs(lower.index(s[i]) - lower.index(s[len(s)-1-i])) for i in range(center))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
