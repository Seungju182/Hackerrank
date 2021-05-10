# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(0, int(input())):
    matches = re.findall(
        r"(#(?:[\da-f]{3}){1,2})(?!\w)(?=.*;)", input(), re.IGNORECASE)
    for m in matches:
        print(m)
