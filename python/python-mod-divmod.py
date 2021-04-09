# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    result = divmod(a, b)
    print(*result, result, sep='\n')
