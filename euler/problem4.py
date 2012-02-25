import numpy
import numpy.testing

#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


#1. Create  3-digits numbers array
a = numpy.arange(100, 1000)
numpy.testing.assert_equal(100, a[0])
numpy.testing.assert_equal(999, a[-1])

#2. Create products array
numbers = numpy.outer(a, a)
numbers = numpy.ravel(numbers)
numbers.sort()
numpy.testing.assert_equal(810000, len(numbers))
numpy.testing.assert_equal(10000, numbers[0])
numpy.testing.assert_equal(998001, numbers[-1])

#3. Find largest palindromic number
for i in xrange(-1, -1 * len(numbers), -1):
   s = str(numbers[i])

   if s == s[::-1]:
      print s
      break
