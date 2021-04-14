# Enter your code here. Read input from STDIN. Print output to STDOUT
_, A = int(input()), set(map(int, input().split()))
N = int(input())

for i in range(N):
    command = input().split()[0]
    getattr(A, command)(set(map(int, input().split())))

print(sum(A))
