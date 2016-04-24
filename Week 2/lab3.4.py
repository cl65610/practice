import pandas as pd
import numpy as np

df = pd.read_csv('crunchbase_monthly_export.csv')

x='one time'
print x
g = lambda x: x*2
print g(x)
print g(45)

df.dropna(0, inplace=True)
print df
