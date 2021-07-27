#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#


def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    if p > s:
        return 0
    k = 1 + (p - m) // d
    dif_price = p * k - ((k - 1) * k * d) // 2
    if dif_price <= s:
        return k + (s - dif_price) // m
    else:
        return math.floor(((m + 2*p) - math.sqrt((m + 2*p)**2 - 8 * m * s)) / 2 * m)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
