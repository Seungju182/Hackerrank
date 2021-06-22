#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#


def breakingRecords(scores):
    # Write your code here
    current_min = scores[0]
    current_max = scores[0]
    count_min = 0
    count_max = 0
    for score in scores:
        if score < current_min:
            current_min = score
            count_min += 1
        elif score > current_max:
            current_max = score
            count_max += 1
    return count_max, count_min


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
