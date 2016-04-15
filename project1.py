import numpy as np

import csv
import urllib2

# url = 'https://raw.githubusercontent.com/ga-students/DSI-DC-1/master/week-01/project-01/assets/sat_scores.csv'
# response = urllib2.urlopen(url)
# data = []
# with open('sat_scores.csv', 'U') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         data.append(row)
# f.close()
# data.pop(0)
# print data
data = [['CT', '82', '509', '510'], ['NJ', '81', '499', '513'], ['MA', '79', '511', '515'], ['NY', '77', '495', '505'], ['NH', '72', '520', '516'], ['RI', '71', '501', '499'], ['PA', '71', '500', '499'], ['VT', '69', '511', '506'], ['ME', '69', '506', '500'], ['VA', '68', '510', '501'], ['DE', '67', '501', '499'], ['MD', '65', '508', '510'], ['NC', '65', '493', '499'], ['GA', '63', '491', '489'], ['IN', '60', '499', '501'], ['SC', '57', '486', '488'], ['DC', '56', '482', '474'], ['OR', '55', '526', '526'], ['FL', '54', '498', '499'], ['WA', '53', '527', '527'], ['TX', '53', '493', '499'], ['HI', '52', '485', '515'], ['AK', '51', '514', '510'], ['CA', '51', '498', '517'], ['AZ', '34', '523', '525'], ['NV', '33', '509', '515'], ['CO', '31', '539', '542'], ['OH', '26', '534', '439'], ['MT', '23', '539', '539'], ['WV', '18', '527', '512'], ['ID', '17', '543', '542'], ['TN', '13', '562', '553'], ['NM', '13', '551', '542'], ['IL', '12', '576', '589'], ['KY', '12', '550', '550'], ['WY', '11', '547', '545'], ['MI', '11', '561', '572'], ['MN', '9', '580', '589'], ['KS', '9', '577', '580'], ['AL', '9', '559', '554'], ['NB', '8', '562', '568'], ['OK', '8', '567', '561'], ['MO', '8', '577', '577'], ['LA', '7', '564', '562'], ['WI', '6', '584', '596'], ['AR', '6', '562', '550'], ['UT', '5', '575', '570'], ['IA', '5', '593', '603'], ['SD', '4', '577', '582'], ['ND', '4', '592', '599'], ['MS', '4', '566', '551']]
# Create a list of state names from the data.

data_master = {}

for x in data:
    data_master[x[0]] = [x[1], x[2], x[3]]


state_names =[x[0] for x in data]

# Print the types of each column
# Column 1 Data type. This is a string, which it should be.
print type(data[0][0])

#Column 2 data type, this is a string, but it should be a float, since it's a %
print type(data[0][1])
for x in data:
    x[1] = float(x[1])/100.0 #Changed the type to float, as well as percent.

#Column 3 data type is string, needs to be changed to an integer
print type(data[0][2])
for x in data:
    x[2] = int(x[2])

# Column 4 data type is a string, needs to be changed to an integer.
print type(data[0][3])
for x in data:
    x[3] = int(x[3])

#Create a dictionary for each column
#Investigate if a list comprehension would be quicker for this
rate_dict = {}
for x in data:
    rate_dict[x[0]] = [x[1]]


verbal_dict = {}
for x in data:
    verbal_dict[x[0]] = [x[2]]

math_dict = {}
for x in data:
    math_dict[x[0]] = [x[3]]

# Print the min and max of each column
# The min of rate is below
# print rate_dict
# mins = [x for x in rate_dict if rate_dict[x] == min(rate_dict.itervalues())]
# print 'Minimum states are', [x for x in rate_dict if x in mins], 'with a rate of', min(rate_dict.itervalues())

# To make this easier, I creatd a formula that will accept a dictionary as an
# argument and return the max and min values.

def min_max(dict):
    mins = [x for x in dict if dict[x] == min(dict.itervalues())]
    maxes = [x for x in dict if dict[x] == max(dict.itervalues())]
    if len(mins) > 1:
        print 'The states with the lowest values are: ' , mins
    else:
        print 'The state with the lowest value is: ', mins
    if len(maxes) > 1:
        print 'The states with the highest values are: ', maxes
    else:
        print 'The state with the highest value is: ', maxes


print verbal_dict
min_max(verbal_dict)

#Write a function that calculates the standard deviation

def stdev(dict):
    st_dev = np.std([dict[x] for x in dict])
    print st_dev
