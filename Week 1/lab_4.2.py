import numpy as np
#Create a one-dimensional array
x = np.array([x for x in range(1,30, 2)])
#print the shape of the array
print (x.shape)
print x
#create a two-dimensional array
x2 = np.matrix([[2,3], [3,4], [x**4 for x in range(5,7)], [11, 44], [4**2, 3**4], [5, 7]])
print x2
print x2.shape
#reshape the array to 2x6
x2 = np.reshape(x2, (2,6))
print x2

#reshape the array to 1x12
x2 = np.reshape(x2, (1,12))
print x2
#Transpose the array
x2 = np.transpose(x2)
print x2
#Ways to Index

#Indexing something from a 3-dimensional array using standard indexing
x3 = np.random.randint(0,high=10,size=(3,3,3))
print x3
print x3[1][2][2]
#Indexing from 2-D array, single-element indexing
x4 = np.random.randint(0,30, size=(4,5))
print x4
#Indexing via array
xa = x4[np.array([2,2,3,2])]
print xa

#Index via slicing 1-d
x3 = np.random.randint(0,high=10,size=(25))
print x3[3:10]
#Index via slicing with steps
x3 = np.random.randint(0,high=10,size=(27))
print x3[4:10:3]

#Index via slicing w/ a 2-D array
x3 = np.random.randint(0,high=10,size=(5,5))
print x3
print x3[1:3, 2:4]

#index with ellipsis and 2-d array
print x3[...,3]

#Ellipsis indexing with 3-d array
x3 = np.random.randint(0,high=10,size=(3,3,7))
print x3
print x3[...,2]
