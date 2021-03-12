# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

print(*product(a, b))
