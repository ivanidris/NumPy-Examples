import numpy

#The sum of the squares of the first ten natural numbers is,
#1 ** 2 + 2 ** 2 + ... + 10 ** 2 = 385

#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10) ** 2 = 55 ** 2 = 3025

#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# 1. Create an array with the first 100 natural numbers
a = numpy.arange(101)

# 2. Sum the squares of the numbers
sum_squares = numpy.sum(a ** 2) 

# 3. Square the sum of the numbers
square_sum = a.sum() ** 2

# Calculate the difference
print square_sum - sum_squares 
