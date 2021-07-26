#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def minimumDistances(a):
    # Write your code here
    min_ = len(a)
    idx = {}
    for index, number in enumerate(a):
        if number in idx:
            distance = index - idx[number]
            min_ = min(min_, distance)
        idx[number] = index
    if min_ != len(a):
        return min_
    else:
        return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
