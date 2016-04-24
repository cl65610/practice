import numpy as np
#Formula that accepts a list as an argument and computes the standard deviation of that list
def st_dev(list):
    dev_sum = 0.0
    mean = sum(list)/len(list)
    for n in list:
        dev_sum += (n - mean)**2
    mean_dev = (dev_sum/len(list))
    std = mean_dev**0.5
    print 'Standard Deviation is: ', std
    return std

list = [i for i in np.random.randint(1, 50, 25)]
print list

st_dev(list)

print 'Numpy Check', np.std(list)

# A formula to check the variance of a data set. Takes a list of  numbers,
# Passes those numbers through a standard deviation formula, and then squares the returned value1
def variance(list):
    dev_sum = 0.0
    mean = sum(list)/len(list)
    for n in list:
        dev_sum += (n-mean)**2
    var = dev_sum/len(list)
    print 'Variance is: ', var
    return var

variance(list)
print 'Numpy variance check', np.var(list)
