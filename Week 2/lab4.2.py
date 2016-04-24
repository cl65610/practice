import scipy as sp
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import norm

random = norm.rvs(size=3)
random

random = norm.rvs(size=5, random_state=1234)
random

n, min_max, mean, var, skew, kurt = stats.describe(random)
print("Number of elements: {0:d}".format(n))
print("Minimum: {0:8.6f} Maximum: {1:8.6f}".format(min_max[0], min_max[1]))
print("Mean: {0:8.6f}".format(mean))
print("Variance: {0:8.6f}".format(var))
print("Skew : {0:8.6f}".format(skew))
print("Kurtosis: {0:8.6f}".format(kurt))

random = norm.rvs(size=50, random_state=123)
random

random_nicole = norm.rvs(size=50, random_state=123456)
n, min_max, mean, var, skew, kurt = stats.describe(random_nicole)
print('Number of elements: {0:d}'.format(n))
print stats.describe(random)
print 'Number of elements: {0:d}'.format(n)
print 'Minimum: {0:8.6f} Maximum: {1:8.6f}'.format(min_max[0], min_max[1])
print 'Mean: {0:8.6f}'.format(mean)
print 'Variance: {0:8.6f}'.format(var)
print 'Skew: {0:8.6f}'.format(skew)
print 'Kurtosis: {0:8.6f}'.format(kurt)

''' Skewness is a measure of how symmetrical the data is. In other words, it tells you how evenly
the data falls about the mean. Something that is perfectly symmetrical would have a skew value of 0.
A positive skew shows that the data is right-leaning, or more of the distribution falls to the right/positive
side of the mean. A negative skew is left-leaning or has more values falling to the left of mean.

Kurtosis is a mesure of how closely a population sample follows a gaussian distribution. In other words,
it also shows how 'tailed' a distribution is. A negative kurtosis indicates a flatter distribution,
or a distribution with fatter tails. A positive kurtosis has a more peaked distribution or shorter tails.
'''
