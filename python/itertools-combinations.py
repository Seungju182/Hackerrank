# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations


def print_combinations(S, N):
    for i in range(1, N+1):
        cb_list = list(combinations(sorted(S), i))
        print(*[''.join(item) for item in cb_list], sep='\n')


if __name__ == "__main__":
    S, N = input().split()
    N = int(N)
    print_combinations(S, N)
