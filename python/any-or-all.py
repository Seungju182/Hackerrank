# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
integers = input().split()

print(all([int(x) > 0 for x in integers])
      and any([x == x[::-1] for x in integers]))
