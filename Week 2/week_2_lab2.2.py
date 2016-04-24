import pandas as pd
import numpy as np
from scipy import stats
data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(data, columns =
                  ['name', 'age', 'preTestScore', 'postTestScore'])
#Select teh preTestScore colukmn

print 'Pre-Test Scores are\n%r' % df['preTestScore']

#Find the Standard Deviation of preTestScore

print 'The Standard Deviation of preTestScore is %r.' % np.std(df['preTestScore'])

# select rows in preTestScore with scores greater than the mean
# find the mean of preTestScore
pre_mean = np.mean(df['preTestScore'])

print 'The mean of pre-test scores is %r.' % pre_mean
df2 = df.loc[df['preTestScore'] > pre_mean]
print 'Pre-Test scores higher than the mean are listed below.'
print df2

# create a new column that shows the score change from
# preTestScore to postTestScore
df['ScoreChange'] = df['postTestScore'] - df['preTestScore']


#Bonus
#Find mean, median, mode, and st. dv of age.
age_mode = stats.mode(df['age'])
print 'The mean of age is %.2f The median is %.2f. The mode is %r, and the standard deviation is %.2f' %(np.mean(df['age']), np.median(df['age']), age_mode[0], np.std(df['age']))
