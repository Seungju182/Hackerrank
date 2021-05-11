# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

# create a subclass and override the handler methods


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for att in attrs:
            print('->', att[0], '>', att[1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for att in attrs:
            print('->', att[0], '>', att[1])


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

N = int(input())

for _ in range(N):
    parser.feed(input())
