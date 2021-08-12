#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def alternate(s):
    # Write your code here
    if len(s) < 2:
        return 0
    letters = list(set(s))
    max_len = 0
    for i in range(len(letters)):
        for j in range(i+1, len(letters)):
            two_letters_lst = [x for x in s if x ==
                               letters[i] or x == letters[j]]
            for k in range(1, len(two_letters_lst)):
                if two_letters_lst[k-1] == two_letters_lst[k]:
                    two_letters_lst = []
                    break
            max_len = max(max_len, len(two_letters_lst))
    return max_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
