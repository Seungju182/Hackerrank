import numpy

coef = numpy.array(input().split(), float)
x = int(input())

print(numpy.polyval(coef, x))
