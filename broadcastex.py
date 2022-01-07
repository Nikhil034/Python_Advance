import numpy as np


'''arr1=np.array([[10,20,30],[40,50,60],[70,80,90]])

arr2=np.array([10,20,30])

arr3=arr1+arr2
print(arr3)'''

arr1=np.arange(0,60,5)
arr1=arr1.reshape(2,6)
print(arr1)

print("-----------------------------------")

for x in np.nditer(arr1):
    print(x)


arr2=arr1.T
print(arr2)

for y in np.nditer(arr2,op_flags['readwrite']):
                                 y[...]=2*y


print(arr2)                                 
