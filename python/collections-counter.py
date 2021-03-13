# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

num_shoes = int(input())
shoes_list = Counter(map(int, input().split()))
num_customers = int(input())

money_earned = 0
for i in range(num_customers):
    size, price = map(int, input().split())
    if shoes_list[size]:
        money_earned += price
        shoes_list[size] -= 1

print(money_earned)
