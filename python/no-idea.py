# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    n, m = map(int, input().split())
    int_array = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    happiness = 0
    for item in int_array:
        if item in A:
            happiness += 1
        elif item in B:
            happiness -= 1
    print(happiness)
