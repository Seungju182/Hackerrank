import numpy

N, M = map(int, input().split())
arr = numpy.array([input().split() for _ in range(N)], int)
print(numpy.max(numpy.min(arr, axis=1), axis=0))
