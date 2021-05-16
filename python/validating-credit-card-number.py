# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def check_validity(num):
    if re.match(r"[456]\d{3}(-?\d{4}){3}$", num) and not re.search(r"(\d)\1{3}", re.sub("-", "", num)):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        check_validity(input())
