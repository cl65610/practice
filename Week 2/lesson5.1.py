import matplotlib.pyplot as plt
import pandas as pd
# from PIL import Image
# age = [5,10,15,20,25,30]
# height = [30, 45, 100, 120,150,180]


# plt.plot(age,height, color='red', alpha=0.5)
# plt.xlabel('age')
# plt.ylabel('height')
# plt.title('My Growth')
# plt.show()

# Puppy behavior thoroughout the day
# pup_pic = Image.open('http://e2ua.com/data/wallpapers/203/WDF_2411532.jpg')
# pup_pic.show()
# puppy_ranking= [7.5, 6, 2, 5.5, 6.8, 9, 8]
# plt.plot(puppy_ranking, alpha=0.75, color='fuchsia')
# plt.title('Puppy Behavior throughout the day')
# plt.xlabel('Times throughout the day')
# plt.ylabel('Puppy Behavior Score')
# plt.show()

# shows = ['Scandal', 'Real Housewives', 'Catfish', 'Teen Mom']
# ranking = [2,1,3,4]
# x = [1,2,3,4]
# plt.barh(x, ranking, align='center', xerr=0.2, color='green', alpha=0.5)
# plt.yticks(x, shows)
# plt.ylabel('Who likes TV?')
# plt.axis([0,5, 0,5])
# plt.text(3, 2, 'When does the Bachelor start?')
# plt.show()
text = u'&#10084'
test = str(text)
print text
import matplotlib.pyplot as plt
import pandas as pd

df = {'name': ['Amndaa', 'Lauren H.', 'Lauren B.', 'JoJo'],
    'job': ['Nutrition', 'Teacher', 'Flight Attendant', 'Flipper'],
    'age': [25, 26, 27, 28],
    'max_week':[4, 8, 12, 12]}
bach = pd.DataFrame(df, columns=['name', 'job', 'age', 'max_week'])
print bach

plt.scatter(bach['age'], bach['max_week'], marker=('5, 1, 0)', color ='purple', alpha = 0.75, s=300)
# plt.set_markersize(5)
plt.xlabel('age')
plt.ylabel('Week They Lasted To')
plt.text(27, 4, 'hey, gurl!')
plt.show()
