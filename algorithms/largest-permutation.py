#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def largestPermutation(k, arr):
    # Write your code here
    d = {k: v for v, k in enumerate(arr)}
    i = 0
    count = 0
    while i < len(arr) - 1 and count < k:
        if arr[i] != len(arr) - i:
            m = len(arr) - i
            arr[i], arr[d[m]] = arr[d[m]], arr[i]
            d[arr[d[m]]], d[m] = d[m], i
            count += 1
        i += 1
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
