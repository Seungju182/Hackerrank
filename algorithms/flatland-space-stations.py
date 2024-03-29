#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.


def flatlandSpaceStations(n, c):
    c.sort()
    # initial distance: first station to first city or last station to last city
    max_ = max(c[0], n - 1 - c[-1])
    for i in range(len(c) - 1):
        max_ = max(max_, (c[i+1] - c[i]) // 2)
    return max_


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
