# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    num_cases = int(input())
    for i in range(num_cases):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)
