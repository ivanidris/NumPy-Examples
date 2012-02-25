import numpy

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 1. Create a divisors array
divisors = numpy.arange(11, 21)

for i in xrange(2520, 10 ** 9, 2520):
        # 2. Check for 0 remainder
        if numpy.all((i % divisors) == 0):
                print i
                # 3. Test the solution
                numpy.testing.assert_equal(numpy.zeros(19), i % numpy.arange(2, 21))
                break

