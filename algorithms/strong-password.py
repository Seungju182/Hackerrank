#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    words = {'numbers': "0123456789", 'lower_case': "abcdefghijklmnopqrstuvwxyz",
             'upper_case': "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 'special_characters': "!@#$%^&*()-+"}
    count = 4
    for case in words:
        if set(password) & set(words[case]):
            count -= 1
    if n + count < 6:
        return 6 - n
    else:
        return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
