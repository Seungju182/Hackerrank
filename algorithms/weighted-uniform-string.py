#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#


def weightedUniformStrings(s, queries):
    # Write your code here
    weights = dict(zip(ascii_lowercase, range(1, len(ascii_lowercase) + 1)))
    temp = set()
    count = 1
    for idx, letter in enumerate(s):
        if idx > 0:
            if s[idx - 1] == letter:
                count += 1
            else:
                count = 1
            temp.add(weights[letter] * count)
        else:
            temp.add(weights[letter])
    return ["Yes" if x in temp else "No" for x in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
