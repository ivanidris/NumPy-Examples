from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import numpy
import sys
import matplotlib.pyplot

#1. Get close prices.
today = date.today()
start = (today.year - 1, today.month, today.day)

quotes = quotes_historical_yahoo(sys.argv[1], start, today)
close =  numpy.array([q[4] for q in quotes])

#2. Get positive log returns.
logreturns = numpy.diff(numpy.log(close))
pos = logreturns[logreturns > 0]

#3. Get frequencies of returns.
counts, rets = numpy.histogram(pos)
rets = rets[:-1] + (rets[1] - rets[0])/2
freqs = 1.0/counts
freqs =  numpy.log(freqs)

#4. Fit the frequencies and returns to a line.
p = numpy.polyfit(rets,freqs, 1)

#5. Plot the results.
matplotlib.pyplot.plot(rets, freqs, 'o')
matplotlib.pyplot.plot(rets, p[0] * rets + p[1])
matplotlib.pyplot.show()
