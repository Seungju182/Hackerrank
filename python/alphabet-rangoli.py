from string import ascii_lowercase as as_lw


def print_rangoli(size):
    # your code goes here
    alphabets = as_lw
    output = []
    for i in range(size):
        letters = "-".join(alphabets[i:n])
        output.append((letters[::-1]+letters[1:]).center(4*n-3, "-"))
    print(*(output[::-1]+output[1:]), sep="\n")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
