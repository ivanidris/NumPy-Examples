from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import numpy
import sys
import scipy.stats
import matplotlib.pyplot

#1. Get close prices.
today = date.today()
start = (today.year - 1, today.month, today.day)

quotes = quotes_historical_yahoo(sys.argv[1], start, today)
close =  numpy.array([q[4] for q in quotes])

#2. Get log returns.
logreturns = numpy.diff(numpy.log(close))

#3. Calculate breakout and pullback
freq = 1/float(sys.argv[2])
breakout = scipy.stats.scoreatpercentile(logreturns, 100 * (1 - freq) )
pullback = scipy.stats.scoreatpercentile(logreturns, 100 * freq)

#4. Generate buys and sells
buys = numpy.compress(logreturns < pullback, close)
sells = numpy.compress(logreturns > breakout, close)
print buys
print sells 
print len(buys), len(sells)
print sells.sum() - buys.sum()

#5. Plot a histogram of the log returns
matplotlib.pyplot.hist(logreturns)
matplotlib.pyplot.show()

#AAPL 50
#[ 340.1   377.35  378.    373.17  415.99]
#[ 357.    370.8   366.48  395.2   419.55]
#5 5
#24.42
