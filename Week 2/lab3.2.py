import pandas as pd
import numpy as np

df = pd.read_csv('rock.csv')
# print df

df_artist = pd.pivot_table(df, index = ['ARTIST CLEAN', 'Release Year'], values='PlayCount')
print df_artist
