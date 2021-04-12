# Enter your code here. Read input from STDIN. Print output to STDOUT
def len_difference(a: set, b: set):
    return len(a.difference(b))


if __name__ == "__main__":
    _, a = int(input()), set(map(int, input().split()))
    _, b = int(input()), set(map(int, input().split()))
    print(len_difference(a, b))
