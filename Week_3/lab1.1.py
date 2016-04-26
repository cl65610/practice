# Download the data, save to a file called "housing.data"
import urllib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"
urllib.urlretrieve (data_url, "housing.data")
# Column names are not included in the data, so a list is created
# in order to add them in later.
names = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE",
         "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"]

df = pd.read_csv('housing.data', header=None, names=names, delim_whitespace=True)
#Look at the first five rows, make sure that the data got imported correctly
df.head()
# The shape function shows us what the data looks like. This particular data frame
# has 506 rows and 14 columsn
df.shape
#This shows what the summary statistics are for these 13 categories.
df.describe()
#Let's start with a simple distribution of the Median Home Values, so that we
# can get a sense of what we're working with.
# sns.distplot(df.MEDV,bins=50,kde=True, axlabel='Median Home Value Distribution', rug=True)
# plt.show()
#This is utterly useless.
# sns.lmplot(x='MEDV', y='NOX', hue='CHAS', data=df)

# for col in df.columns:
#     sns.jointplot(x='MEDV', y=col, data=df)

# The next few lines create png files comparing all the data points. The one titled
# g singles out median values vs. everything else. Big is a pure pairplot of everything

g= sns.pairplot(x_vars='MEDV', y_vars=df.columns, data =df)
big = sns.pairplot(df)
big.savefig('bigpairplot.png')
g.savefig('pairplot.png')

"""Data Analysis
Looking at the 13 values plotted against Median Home value, there are a few interesting
relationships. Not surprisingly, there's some kind of relationship between crime rates
and median house values, but it doesn't look exactly linear. Below a certain threshold(around 0.15), crime
rates don't seem to have too much effect on house values.

The variables that have the strongest correlation appear to be number of rooms in
the house(RM), the proportion of African Americans by town (B), and the percentage
of lower class people living in the area (Although this variable(LSTAT) doesn't appear
to be strictly linear).

A few other have what appear to be weak relationships. Things like the ppm of NO
in the air are roughly correlated with home value. Distance from town and Student
Teacher relationship are similarly correlated. Most of the other variables have no
obvious relationship with the median home value.

Other Relationships:

In no particular order, there appear to be relationships between the following
variables:

Weighted distance from town(DIS) and square area of industrial space (INDUS)

PPM of Nitrous Oxides (NO) has a relationship with Industrial zones (INDUS) and
Distance from town (DIS). This makes some sense. NOs are a byproduct of factories,
so they should occur more frequently away from town.

Number of rooms/dwelling (RM) is connected to the proporiton of lower status
citizens (LSTAT)

There's an interesting relationship between the age of a home (AGE) and its
distance from town (DIS)

Other variables have weaker relationships. It'll be interesting to see how these
variables interact with each other. For example taking proximity to the Charles
River into account when looking at home values and distance from town. 
