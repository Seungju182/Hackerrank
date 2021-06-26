#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#


def dayOfProgrammer(year):
    # Write your code here
    is_leap = year % 4 == 0 and (year < 1918 or year %
                                 100 != 0 or year % 400 == 0)
    if year == 1918:
        return "26.09.{}".format(year)
    elif is_leap:
        return "12.09.{}".format(year)
    else:
        return "13.09.{}".format(year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
