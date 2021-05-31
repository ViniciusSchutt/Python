import numpy #So we can use the numpy functions on arrays
#declaring the array
array = numpy.array([[1, 2], [3, 4]])

sum = numpy.sum(array, axis=0) #making the sum
product = numpy.prod(array, axis=None) #and the product

print(f'The product of the arrays is: {product}\n')
