# ARRAY PROPERTIES
# How to use size() property

import numpy as np 
# create a 2-D array
a=np.array([[10,20,30],[1,2,3],[7,8,9]])
print(a)
# check the size of the array
b=np.size(a)
print(b)

# How to use shape() property

c= np.shape(a)
print(c)


# How to use dtype() property

d=a.dtype
print(d)

# How to use ndim() property

# create a 2-D array 
array1 = np.array([[2, 4, 6],
                  [1, 3, 5]])

# check the dimension of array1
print(array1.ndim) 

# How to use itemize() property

# create a default 1-D array of integers
array2 = np.array([6, 7, 8, 10, 13],dtype=np.int64)

# create a 1-D array of 32-bit integers 
array3 = np.array([6, 7, 8, 10, 13], dtype=np.int32)

# use of itemsize to determine size of each array element of array1 and array2
print(array2.itemsize)  
print(array3.itemsize) 
print(array1.itemsize)

# How to use data() property # its print memory address of the arrays

array1 = np.array([6, 7, 8])
array2 = np.array([[1, 2, 3],[6, 7, 8]])

# print memory address of array1's and array2's data
print("\nData of array1 is: ",array1.data)
print("Data of array2 is: ",array2.data)