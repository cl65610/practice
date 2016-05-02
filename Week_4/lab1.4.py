import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
% matplotlib inline

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data', header=None) # Read in
# the data from the illinois state website

df.head() # Take a look at it, make sure it's reading properly
# After reading the documentation, it seems like the target field should
# be whether or not a sample tested malignent or benign. The data fields that follow
# this field will be the features. The specifics of what these numbers indicate
# is largely irrelevant for our purposes. All we need to do is use them to make a model
# that will evaluate the same criteria in future patients.

target = df[1].astype('category') # Set the target field
features = df.ix[:, 3:] # Set the features
features.head()
target.head()
values = target.value_counts()

target.describe()
