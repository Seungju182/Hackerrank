# Enter your code here. Read input from STDIN. Print output to STDOUT
def criterion(x):
    if x.isdigit():
        if int(x) % 2 == 0:
            return (3, x)
        else:
            return (2, x)
    elif x.isupper():
        return (1, x)
    elif x.islower():
        return (0, x)


print(*sorted(input(), key=criterion), sep='')
