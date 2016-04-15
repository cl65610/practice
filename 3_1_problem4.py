import numpy as np
for i in range(1, 15, 2):
    numbers = [round(abs(x*np.random.randn())) for x in np.random.gamma(i, i, 100)]

def rand_stats(i, numbers):
    for i in range(1,15,2):
        print 'i is currently %d.' % i
        print 'mean: ' ,(sum(numbers)/len(numbers))
        print '\tmedian: ' , np.median(numbers)

rand_stats(i,numbers)
