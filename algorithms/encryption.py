#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def encryption(s):
    # Write your code here
    text = s.replace(' ', '')
    n_col = math.ceil(math.sqrt(len(text)))
    result = []
    for i in range(n_col):
        num = i
        x = ''
        while num < len(text):
            x = ''.join([x, text[num]])
            num += n_col
        result.append(x)
    return ' '.join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
