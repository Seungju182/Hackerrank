#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    i = 1
    out = 1
    while i <= n:
        out *= i
        i += 1
    print(out)    

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
