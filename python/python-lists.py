"""
There are some other ways to solve this problem like using eval function or getattr function.
But I just used simple if-else statement for better understanding.
"""
if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        args = input().split()
        command = args.pop(0)
        num = list(map(int, args))
        if command == 'insert':
            arr.insert(num[0], num[1])
        elif command == 'print':
            print(arr)
        elif command == 'remove':
            arr.remove(num[0])
        elif command == 'append':
            arr.append(num[0])
        elif command == 'sort':
            arr.sort()
        elif command == 'pop':
            arr.pop()
        elif command == 'reverse':
            arr.reverse()
