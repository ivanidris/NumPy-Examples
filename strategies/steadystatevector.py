#!/usr/bin/env python

from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import numpy
import sys

today = date.today()
start = (today.year - 1, today.month, today.day)

quotes = quotes_historical_yahoo(sys.argv[1], start, today)
close =  [q[4] for q in quotes]

states = numpy.sign(numpy.diff(close))

NDIM = 3
SM = numpy.zeros((NDIM, NDIM))

signs = [-1, 0, 1]
k = int(sys.argv[2])

for i in xrange(len(signs)):
   #we start the transition from the state with the specified sign
   start_indices = numpy.where(states[:-1] == signs[i])[0]

   N = len(start_indices) + k * NDIM

   # skip since there are no transitions possible
   if N == 0:
      continue
   
   #find the values of states at the end positions
   end_values = states[start_indices + 1]

   for j in xrange(len(signs)):
      # number of occurrences of this transition 
      occurrences = len(end_values[end_values == signs[j]])
      SM[i][j] = (occurrences + k)/float(N)

print SM
eig_out = numpy.linalg.eig(SM)
print eig_out

idx_vec = numpy.where(numpy.abs(eig_out[0] - 1) < 0.1)
print "Index eigenvalue 1", idx_vec

x = eig_out[1][:,idx_vec].flatten()
print "Steady state vector", x
print "Check", numpy.dot(SM, x)
