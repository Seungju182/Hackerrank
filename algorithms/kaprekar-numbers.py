#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#


def kaprekarNumbers(p, q):
    # Write your code here
    lst = []
    for num in range(p, q+1):
        squared = num ** 2
        d = 10 ** len(str(num))
        if squared // d + squared % d == num:
            lst.append(num)
    if lst:
        print(*lst)
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
