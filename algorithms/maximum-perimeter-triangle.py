#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#


def maximumPerimeterTriangle(sticks):
    # Write your code here
    sticks.sort()
    i = len(sticks) - 1
    while i > 1:
        if sticks[i] < sticks[i-1] + sticks[i-2]:
            return [sticks[i-2], sticks[i-1], sticks[i]]
        else:
            i -= 1
    return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
