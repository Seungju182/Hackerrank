# Enter your code here. Read input from STDIN. Print output to STDOUT.
import re


def detector(text):
    return bool(re.match("^[\+-]?\d*\.\d+$", text))


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        print(detector(input()))
