import numpy as np

'''arr=np.array([[1,2],[3,4],[5,6]])
print(arr)

y=arr[[0,2],[1,1]]
print(y)'''

'''arr2=np.array([[0,1,2],[3,4,5],[6,7,8]])
print(arr2)

rows=np.array([[0,0],[2,1]])
cols=np.array([[0,2],[0,1]])
y=arr2[rows,cols]
print(y)
x=arr2[1:4,1:3]
print('\n',x)

bl=arr2[arr2>5]
print(bl)'''

#broadcasting

a=np.array([1,2,3,4])
b=np.array([10,20,20,10])
c=a*b;
print(c)


