# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict


def check_appearance(n, m):
    d = defaultdict(list)
    for i in range(n):
        letter = input()
        # change type to string for printing out the result
        d[letter].append(str(i+1))
    letters_to_be_checked = [input() for i in range(m)]
    print(*[" ".join(d[letter]) if letter in d else -
            1 for letter in letters_to_be_checked], sep='\n')


if __name__ == '__main__':
    n, m = map(int, input().split())
    check_appearance(n, m)
