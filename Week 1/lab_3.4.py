import numpy as np
from numpy import mean, median
from scipy.stats import mode
lab_list = [0,0, 2.3, 5**2, 5**0.5, 5, 700, 67, -34, 35, 36, 38, 49, -34, 26-1, 23+2]

lab_mean = mean(lab_list)
print 'The median is %.2f.' % lab_mean

lab_med = median(lab_list)
print 'The median is %.2f.' % lab_med

lab_mode = mode(lab_list)
print  'The mode is %.2f.' % lab_mode.mode[0]

lab_var = np.var(lab_list)
print 'The variance is %.2f.' % lab_var

lab_dev = np.std(lab_list)
print 'The standard deviation is %.2f.' % lab_dev


def no_more_negatives(list):
    for n in list:
        if n < 0:
            list.remove(n)
    print 'Here\'s your list without any negative numbers: ' ,list

no_more_negatives(lab_list)
