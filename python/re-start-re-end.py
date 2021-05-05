# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()
k = input()

matches = list(re.finditer(r'(?={})'.format(k), S))

if matches:
    print(*[(match.start(), match.start() + len(k) - 1)
            for match in matches], sep='\n')
else:
    print((-1, -1))
