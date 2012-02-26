import numpy
import numpy.testing

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a ** 2 + b ** 2 = c ** 2
#
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#1. Create m and n arrays
m = numpy.arange(33)
n = numpy.arange(33)

#2. Calculate a, b and c
a = numpy.subtract.outer(m ** 2, n ** 2)
b = 2 * numpy.multiply.outer(m, n)
c = numpy.add.outer(m ** 2, n ** 2)

#3. Find the index
idx =  numpy.where((a + b + c) == 1000)

#4. Check solution
numpy.testing.assert_equal(a[idx]**2 + b[idx]**2, c[idx]**2)
print a[idx] * b[idx] * c[idx]
