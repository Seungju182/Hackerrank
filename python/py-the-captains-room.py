# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
room_numbers = list(map(int, input().split()))

first = set()
existing = set()

for room in room_numbers:
    if room in first:
        existing.add(room)
    else:
        first.add(room)

print(first.difference(existing).pop())
