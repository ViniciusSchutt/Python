import numpy

my_array = numpy.array([[1, 2], [3, 4]])

su = numpy.sum(my_array, axis=0)
pr = numpy.prod(my_array, axis=None)

print(pr)
