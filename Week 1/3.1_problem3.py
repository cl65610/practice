list1 = [1.5,3.5,5.5,7.5]
list2 = [0,4,8,12]
iteration = 1
multiplied = 0
while multiplied < 300:
    for a,b in zip(list1, list2):
        value1 = a
        value2 = b
        multiplied = value1*value2
        print multiplied
        print iteration
        iteration += 1
    list1 = [x*2 for x in list1]
    list2 = [x*2 for x in list2]
    print list1
    print list2
