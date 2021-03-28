# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    N = int(input())
    s = set()
    for i in range(N):
        s.add(input())
    print(len(s))
