# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == "__main__":
    N = int(input())
    d = deque()
    for i in range(N):
        command, *value = input().split()
        getattr(d, command)(*(int(x) for x in value))
    print(*d, sep=' ')
