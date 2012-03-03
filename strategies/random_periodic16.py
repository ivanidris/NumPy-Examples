from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import numpy
import sys
import matplotlib.pyplot

def get_indices(high, size):
   #2. Generate random indices
   return numpy.random.randint(0, high, size)

#1. Get close prices.
today = date.today()
start = (today.year - 1, today.month, today.day)

quotes = quotes_historical_yahoo(sys.argv[1], start, today)
close =  numpy.array([q[4] for q in quotes])

nbuys = int(sys.argv[2])
N = int(sys.argv[3])
profits = numpy.zeros(N)

for i in xrange(N):
   #3. Simulate trades
   buys = numpy.take(close, get_indices(len(close), nbuys))
   sells = numpy.take(close, get_indices(len(close), nbuys))
   profits[i] = sells.sum() - buys.sum()

print "Mean", profits.mean() 
print "Std", profits.std()

#4. Plot a histogram of the profits
matplotlib.pyplot.hist(profits)
matplotlib.pyplot.show()

#python random_periodic16.py AAPL 5 2000
#Mean -2.566465
#Std 133.746039463

