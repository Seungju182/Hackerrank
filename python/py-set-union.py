# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n = int(input())
    english = set(map(int, input().split()))
    m = int(input())
    french = set(map(int, input().split()))
    print(len(english.union(french)))
