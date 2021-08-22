#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#


def separateNumbers(s):
    # Write your code here
    def check(s, x):
        if s:
            if s.startswith(x):
                return check(s[len(x):], str(int(x)+1))
            else:
                return False
        return True

    for i in range(1, len(s)//2 + 1):
        sub = s[:i]
        if check(s, sub):
            print("YES", sub)
            return None
    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
