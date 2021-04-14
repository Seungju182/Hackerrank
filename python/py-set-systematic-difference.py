# Enter your code here. Read input from STDIN. Print output to STDOUT
_, A = int(input()), set(map(int, input().split()))
_, B = int(input()), set(map(int, input().split()))
print(len(A.symmetric_difference(B)))
