# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
N = int(input())

strict = True
for _ in range(N):
    test_set = set(map(int, input().split()))
    strict = strict and A.issuperset(test_set) and not(A.issubset(test_set))

print(strict)
