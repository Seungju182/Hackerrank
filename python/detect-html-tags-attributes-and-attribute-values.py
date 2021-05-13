# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])


parser = MyParser()

N = int(input())
for i in range(N):
    parser.feed(input())
