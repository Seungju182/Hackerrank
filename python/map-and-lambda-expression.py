def cube(x): return x**3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    elif n > 2:
        fibonacci_numbers = fibonacci(n-1)
        fibonacci_numbers.append(fibonacci_numbers[-1]+fibonacci_numbers[-2])
        return fibonacci_numbers


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
