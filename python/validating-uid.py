# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def validity_check(uid):
    if re.match(r'^(?!.*(.).*\1)(?=(.*[A-Z]){2,})(?=(.*?[0-9]){3,})[a-zA-Z0-9]{10}$', uid):
        print('Valid')
    else:
        print('Invalid')


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        validity_check(input())
