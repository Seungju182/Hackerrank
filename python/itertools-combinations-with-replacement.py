# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement


def print_replacement_combinations(S, k):
    cb_list = list(combinations_with_replacement(sorted(S), k))
    print(*[''.join(item) for item in cb_list], sep='\n')


if __name__ == "__main__":
    S, k = input().split()
    print_replacement_combinations(S, int(k))
