import pandas as pd
import  numpy as np

df = pd.read_csv('sales.csv')

print df
df2 = pd.pivot_table(df,index=["Manager", "Rep", 'Product'], values = ['Price']
, aggfunc=np.sum, margins=True, fill_value='zero')

# df2.fillna(0, inplace=True)
print(df2)


raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

df = pd.DataFrame(raw_data)
print df

df2 = pd.pivot_table(df, index=['regiment', 'company'], margins=True)
# print df2


#Questions of the data

#1. Which regiment had the best postTestScores

df2 = pd.pivot_table(df, index=['company'], margins=True, columns=['regiment'])
print df2

#2. Who did well

df3 = pd.pivot_table(df,index = ['name'],margins=True, values=['preTestScore', 'postTestScore'], columns=['regiment'], aggfunc=np.sum)
print df3

#3 Who made the most progress?

df4 = pd.pivot_table(df, index=['name'], values=['preTestScore', 'postTestScore'])
df4['progress'] = df4['postTestScore']-df4['preTestScore']
print df4
