import numpy

#Problem 1.
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

# 1. Numbers 1 - 1000
a = numpy.arange(1, 1000)

# 2. Select multiple of 3 or 5
a = a[(a % 3 == 0) | (a % 5 == 0)]
print a[:10]

# 3. Sum the numbers
print a.sum()
