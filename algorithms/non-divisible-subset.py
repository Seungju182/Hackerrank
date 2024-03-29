#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def nonDivisibleSubset(k, s):
    # Write your code here
    counts = [0] * k
    for num in s:
        counts[num % k] += 1
    sum_ = min(counts[0], 1)
    if k % 2:
        return sum_ + sum([max(counts[i], counts[k-i]) for i in range(1, k//2 + 1)])
    else:
        return sum_ + 1 + sum([max(counts[i], counts[k-i]) for i in range(1, k//2)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
