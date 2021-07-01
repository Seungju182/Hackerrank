#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#


def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    if min(keyboards) + min(drives) > b:
        return -1
    else:
        max_ = 0
        for keyboard in keyboards:
            for drive in drives:
                cost = keyboard + drive
                if cost <= b and cost > max_:
                    max_ = cost
        return max_


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
