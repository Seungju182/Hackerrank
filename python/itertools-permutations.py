# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations


def print_permutations(S, k):
    list_permutaions = sorted([''.join(item) for item in permutations(S, k)])
    print(*list_permutaions, sep='\n')


if __name__ == '__main__':
    S, k = input().split()
    k = int(k)
    print_permutations(S, k)
