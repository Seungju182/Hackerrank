# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def convert(line):
    return re.sub(r"(?<= )(&&|\|\|)(?= )", lambda x: "and" if x.group() == "&&" else "or", line)


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        print(convert(input()))
