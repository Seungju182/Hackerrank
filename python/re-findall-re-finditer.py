# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

v = "AEIOUaeiou"
c = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"

print('\n'.join(re.findall(
    r'(?<=[%s])([%s]{2,})[%s]' % (c, v, c), input()) or ['-1']))
