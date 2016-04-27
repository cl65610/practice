#Set up the environment by loading the necessary packages
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm

%matplotlib inline

sacram = pd.read_csv('Sacramentorealestatetransactions.csv')
sacram.tail()
# Show how many counts there are for each city in the city column
print sacram.city.value_counts()
print sacram.dtypes #Sale_date is an object, it doesn't seem to be converted
# to a date by using the 'to_datetime' function of pandas. It's like it doesn't recognize
# it as a valid date.

sacram.describe()

# Visualize the Data: This shows how price correlates with several different factors.
# It doesn't appear that there are any strong correlations between these.
sns.pairplot(x_vars='price', y_vars=['zip', 'beds', 'baths', 'sq__f', 'latitude', 'longitude'], data=sacram)
# This strip plot shows that there isn't a huge difference in home prices between cities.
sns.pairplot(sacram)

sns.stripplot(x='city', y='price', data=sacram, jitter=True)

#Distribution of home prices in Sacramento County
sns.distplot(sacram['price'])

# Create categorical variables for city names
city_dict={}
count=1
for row in sacram['city'].unique():
    city_dict[row]=count
    count +=1
print city_dict
# sacram['city_number'] =

#This regression model shows how well square foot, # of baths, beds, and zip code are
# predictive of home price. The R^2 score for this is 0.19, indicating that this
# model only explains 19% of the model.
lm = linear_model.LinearRegression()
X= sacram[['sq__ft', 'baths', 'beds', 'zip']]
y= sacram['price']
model = lm.fit(X,y)
predictions = lm.predict(X)
print lm.score(X, y)
plt.scatter(predictions, y, s=30, c='r', marker='+', zorder=10)

# This regression shows how well you can predict the number of baths a home has
# if you know it's square footage and the number of beds
lm = linear_model.LinearRegression()
X= sacram[['sq__ft' ,'beds']]
y= sacram['baths']
model = lm.fit(X,y)
predictions = lm.predict(X)
print lm.score(X, y)
plt.scatter(predictions, y, s=30, c='r', marker='+', zorder=10)
sns.regplot(x=predictions, y=y)
