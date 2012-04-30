import numpy
import sys
import matplotlib.pyplot
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import scipy.stats

def random_indices(N):
   return numpy.random.randint(0, N, N)

def random_values(values):
   return numpy.take(values, random_indices(len(values)))
   
def generate_means(values):
   NTRIES = int(sys.argv[2])

   means = numpy.zeros(NTRIES)

   for i in xrange(NTRIES):
      means[i] = random_values(values).mean()

   return means

def format_mean(values):
   return "Mean=%.3f" % (values.mean())

def plot_percentile(values, means):
   matplotlib.pyplot.hist(means)
   percentile = scipy.stats.percentileofscore(means, values.mean())
   matplotlib.pyplot.legend([format_mean(means), "Percentile=%.2f" %(percentile)])

def plot(values):
   matplotlib.pyplot.hist(values)
   matplotlib.pyplot.legend([format_mean(values)])

today = date.today()
start = (today.year - 1, today.month, today.day)
quotes = quotes_historical_yahoo(sys.argv[1], start, today)
close =  numpy.array([q[4] for q in quotes])
close_means = generate_means(close)

normal_values = numpy.random.normal(size=len(close))
normal_means = generate_means(normal_values)

matplotlib.pyplot.subplot(221)
matplotlib.pyplot.title("Close Values")
plot(close)

matplotlib.pyplot.subplot(222)
matplotlib.pyplot.title("Normal Values")
plot(normal_values)

matplotlib.pyplot.subplot(223)
matplotlib.pyplot.title("Close Means")
plot_percentile(close, close_means)

matplotlib.pyplot.subplot(224)
matplotlib.pyplot.title("Normal Means")
plot_percentile(normal_values, normal_means)

matplotlib.pyplot.show()
