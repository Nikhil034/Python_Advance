import numpy as np

'''lst=[10,20,30,40,50]
arr=np.asarray(lst)
print(arr)'''

'''s=b"hello"
a=np.frombuffer(s)
print(a)'''

'''lst=range(5)
it=iter(lst)
arr=np.fromiter(it,dtype=int)
print(arr)'''

'''arr=np.arange(10,20,2)
print(arr)'''

'''arr=np.linspace(10,20,2,endpoint=False)
print(arr)'''

'''arr=np.logspace(1.0,2.0,num=10)
print(arr)
#give log of particular value'''

arr=np.arange(20)
s=slice(2,20,4)
print(arr[s])
