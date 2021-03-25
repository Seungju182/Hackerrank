# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    M = int(input())
    set_M = set(map(int, input().split()))
    N = int(input())
    set_N = set(map(int, input().split()))
    only_M = set_M.difference(set_N)
    only_N = set_N.difference(set_M)
    difference = only_M.union(only_N)
    print(*sorted(difference), sep='\n')
