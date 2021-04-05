# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n, dq = int(input()), deque(map(int, input().split()))
        for cube in sorted(dq, reverse=True):
            if dq[0] == cube:
                dq.popleft()
            elif dq[-1] == cube:
                dq.pop()
            else:
                print('No')
                break
        else:
            print('Yes')
