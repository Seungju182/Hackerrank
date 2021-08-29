#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def closestNumbers(arr):
    # Write your code here
    min_ = math.inf
    arr.sort()
    pairs = []
    for i in range(len(arr) - 1):
        min_ = min(arr[i+1] - arr[i], min_)
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] == min_:
            pairs.extend([arr[i], arr[i+1]])
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
