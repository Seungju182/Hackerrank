#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#


def happyLadybugs(b):
    # Write your code here
    for letter in set(b):
        if letter != "_" and b.count(letter) == 1:
            return "NO"
    if b.count("_") == 0:
        for i in range(1, len(b)-1):
            if b[i] != b[i-1] and b[i] != b[i+1]:
                return "NO"
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
