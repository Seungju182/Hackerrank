import numpy

N, M = map(int, input().split())

A = numpy.array([input().split() for _ in range(N)], int)
B = numpy.array([input().split() for _ in range(N)], int)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
