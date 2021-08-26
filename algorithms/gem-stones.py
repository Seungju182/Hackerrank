#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#


def gemstones(arr):
    # Write your code here
    gem = 0
    first = arr.pop()
    for letter in set(first):
        is_in = True
        for x in arr:
            if letter not in x:
                is_in = False
                break
        if is_in:
            gem += 1
    return gem


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
