# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == "__main__":
    N = int(input())
    letters = input().split()
    K = int(input())
    list_comb = list(combinations(letters, K))
    print(len([c for c in list_comb if 'a' in c]) / len(list_comb))
