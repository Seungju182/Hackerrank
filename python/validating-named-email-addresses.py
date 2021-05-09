# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re

pattern = re.compile(r"^[a-zA-Z][\w\-\.\,\_]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$")


def validate(text):
    name, address = email.utils.parseaddr(text)
    if re.match(pattern, address):
        print(text)


if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        validate(input())
