# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def validate_phone_number(x):
    if re.match(r'[789]\d{9}$', x):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        validate_phone_number(input())
