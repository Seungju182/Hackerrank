#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = input()
    top_3 = Counter(sorted(s)).most_common(3)
    for item in top_3:
        print(item[0], item[1])
