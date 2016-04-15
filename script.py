from random import randint
count = 0
good = ['Go for it', 'Today\'s the day', 'Heck Yeah!']
bad = ['Maybe', 'Go play in traffic', 'In your dreams', 'Not even once', 'No']
while count < 5:
    number = randint(0,7)
    if number < 3:
        print good[number]
        break
    else:
        print bad[number-3]
        print 'rolling again'
        count += 1
