import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

x = [x for x in range(1938, 2017)]
y = []
for i in x:
    y.append(random.gauss(15000, 0.2))
print len(x)
print len(y)
def line_predict(x,y):
    x_mean = np.mean(x)
    y_mean=np.mean(y)
    num = 0
    denom=0
    for x,y in zip(x,y):
        xvar=x-x_mean
        yvar=y-y_mean
        num+=xvar*yvar
        denom+= xvar**2
    m = num/denom

    b = y_mean - m*x_mean
    print m
    print b
    ys = []
    for i in x:
        ys.append(i*m+b)
    return ys
plt.scatter(x,y)
plt.plot(x, line_predict(x,y))
plt.show()
