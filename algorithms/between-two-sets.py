#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

from functools import reduce

def getTotalX(a, b):
    # Write your code here
    def lcm(x,y):
        return x * y // math.gcd(x, y)
    lcm_a = reduce(lcm, a)
    gcd_b = reduce(math.gcd, b)
    count = 0
    if gcd_b % lcm_a == 0:
        x = gcd_b // lcm_a
        for i in range(1, x+1):
            if x % i == 0:
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
