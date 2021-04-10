# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_mode(a, b, m):
    print(pow(a, b))
    print(pow(a, b, m))


if __name__ == "__main__":
    print_mode(int(input()), int(input()), int(input()))
