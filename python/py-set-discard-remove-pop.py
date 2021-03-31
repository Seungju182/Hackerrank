n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command, *value = input().split()
    getattr(s, command)(*(int(x) for x in value))

print(sum(s))
