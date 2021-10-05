#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def formingMagicSquare(s):
    # Write your code here
    def rotate_matrix(m):
        return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1, -1, -1)]

    def flip_matirx(m):
        return [s[::-1] for s in m]

    def check(m, s):
        cur = math.inf
        for _ in range(4):
            m = rotate_matrix(m)
            sum_ = sum([abs(m[i][j] - s[i][j])
                        for j in range(len(s)) for i in range(len(s))])
            if sum_ < cur:
                cur = sum_
        return cur
    magic = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    return min(check(magic, s), check(flip_matirx(magic), s))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
