# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def check_regex(S):
    is_regex = True
    try:
        re.compile(S)
    except re.error:
        is_regex = False
    return is_regex


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        print(check_regex(input()))
