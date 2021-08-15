#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    result = ""
    for i in s:
        if i.isupper():
            start = ord('A')
            i = chr(start + (ord(i) - start + k) % 26)
        elif i.islower():
            start = ord('a')
            i = chr(start + (ord(i) - start + k) % 26)
        result = result + i
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
