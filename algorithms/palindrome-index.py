#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def palindromeIndex(s):
    # Write your code here
    def is_palindrome(x):
        for i in range(len(x)//2):
            if x[i] != x[len(x) - 1 - i]:
                return False
        return True

    for i in range(len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            test = s[:i] + s[i+1:]
            if is_palindrome(test):
                return i
            else:
                return len(test) - i
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
