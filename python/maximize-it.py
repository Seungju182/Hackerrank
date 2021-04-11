# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

K, M = map(int, input().split())

X_list = []
for _ in range(K):
    N, *elements = map(int, input().split())
    X_list.append(elements)

comb_list = product(*X_list)


def sum_squares_mod(l):
    return sum(map(lambda x: x*x, l)) % M


print(max(list(map(sum_squares_mod, comb_list))))
