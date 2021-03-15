# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath


def complex_polar(num):
    print(*cmath.polar(complex(num)), sep='\n')


if __name__ == '__main__':
    complex_polar(input())
