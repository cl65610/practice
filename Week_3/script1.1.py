# #Plotting the line of best fit the hard way
#
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# %matplotlib inline
# # x = [0,1,2,3,4,5]
# # y = [0,1,2,3,4,5]
# #
# #
# # x = np.asarray([0,1,2,3,4,5])
# # y = -2*x
# # plt.plot(x,y, color = 'indigo', alpha = 0.6)
# # plt.show()
#
# xs = range(1938, 2017)
# ys = []
# for i in x:
#     ys.append(random.gauss(15000, 0.2))
#
# # plt.plot(xs, ys)
#
# def beta(xs, ys):
#     numerator = 0
#     denominator = 0
#     x_mean = np.mean(xs)
#     y_mean = np.mean(ys)
#     for x, y in zip(xs, ys):
#         numerator += (x - x_mean) * (y - y_mean)
#         denominator += (x - x_mean) * (x - x_mean)
#     return numerator / denominator
#
# def alpha(xs, ys):
#     m = beta(xs, ys)
#     b = np.mean(ys) - m * np.mean(xs)
#     return b
#
# # Plotting
#
# def predict(xs, ys):
#     b = alpha(xs, ys)
#     m = beta(xs, ys)
#     yhats = [b + m * x for x in xs]
#     return yhats
#
# ps = predict(xs, ys)
#
# # The raw data
# plt.scatter(xs, ys)
# # The best fit line
# plt.plot(xs, ps)
# plt.show()

# Getting into lesson 1.2

from matplotlib import pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std

%matplotlib inline
data = datasets.load_boston()
# print data.DESCR
# print data.feature_names
# print data.data[0]
# print data.target[0]
import numpy as np
import pandas as pd
df = pd.DataFrame(data.data, columns=data.feature_names)
# print df.head()

targets = pd.DataFrame(data.target, columns=['MEDV'])
# print targets.head()

lm = linear_model.LinearRegression()
X= df[['RM']]
y= targets['MEDV']
model = lm.fit(X,y)
predictions = lm.predict(X)
print lm.score(X, y)

plt.scatter(predictions, y, s=30, c='r', marker='+', zorder=10)
