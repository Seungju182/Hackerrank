#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


def makingAnagrams(s1, s2):
    # Write your code here
    duplicates = set(s1).intersection(set(s2))
    c1 = Counter(s1)
    c2 = Counter(s2)
    sum_ = sum([2 * min(c1[i], c2[i]) for i in set(s1) if i in duplicates])
    return len(s1) + len(s2) - sum_


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
