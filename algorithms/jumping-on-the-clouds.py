#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#


def jumpingOnClouds(c):
    # Write your code here
    start = 0
    score = 0
    for idx, num in enumerate(c):
        if num:
            score += math.ceil((idx - 1 - start) / 2) + 1
            start = idx + 1
    if len(c) > start + 1:
        score += math.ceil((len(c) - 1 - start) / 2)
    return score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
