#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        return -1
    else:
        s_1 = Counter(s[:len(s)//2])
        s_2 = Counter(s[len(s)//2:])
        count = 0
        for item in s_1:
            count += max(s_1[item] - s_2.get(item, 0), 0)
        return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
