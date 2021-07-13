#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c, k):
    n = len(c)
    i = k % n
    e = 100 - (c[i] * 2 + 1)
    while i:
        i = (i + k) % n
        e -= c[i] * 2 + 1
    return e


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
