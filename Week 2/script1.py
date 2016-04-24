import pandas as pd
import numpy as np
# three columns of 10 random numbers in a dataframe
s = pd.DataFrame(np.random.randn(10, 3), columns=['rand1', 'rand2', 'rand3'])

#reindexing the DataFrame

s2 = s.reindex([1,2,3,4,5,6,7,8,9,0])

#Sort column 'rand1' in ascending order
s2 = s.sort_values('rand1')
print s2

#Vectorized operations
#Multiplied column values by 2
s2['rand1'] = s2['rand1']*2
#Create new column with vales of column 1 and 2 added together
s2['sumrand1+2'] = s2['rand1']+s2['rand2']

s3 = s2[s>0]
print s3
