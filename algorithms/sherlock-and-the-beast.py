#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#


def decentNumber(n):
    # Write your code here
    num = n // 3
    while num >= 0:
        x = n - num * 3
        if x % 5 == 0:
            five = "5" * num * 3
            three = "3" * x
            print(int(five+three))
            return
        else:
            num -= 1
    print(-1)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
