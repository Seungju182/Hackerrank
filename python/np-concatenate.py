import numpy

N, M, P = map(int, input().split())

array_n = numpy.array([input().split() for _ in range(N)], int)
array_m = numpy.array([input().split() for _ in range(M)], int)
print(numpy.concatenate((array_n, array_m), axis=0))
