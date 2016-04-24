import pandas as pd
import numpy as np

df = pd.read_csv('crunchbase_monthly_export.csv')

print df.head()
print df[' market ']
print df.columns
#print pd.get_dummies(df['country_code'])
print df[' market '].nunique()

print df.dtypes
def no_commas(string):
    for x in string:
        if x == ',':
            x.replace(',', '', inplace=True)
df[' funding_total_usd '] = df[' funding_total_usd '].apply(no_commas)

print df[' funding_total_usd ']

    # x.replace(',', '', inplace=True)

# df[' funding_total_usd '] = df[' funding_total_usd '].astype()
