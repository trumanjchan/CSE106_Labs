# Problem 1
import numpy as np
print()

arr1 = np.arange(2, 10, 1).reshape(4,2)
print("-- A 4x2 matrix with values ranging from 2 to 10 --")
print(arr1)

arr2 = np.ones( (8, 8) )
arr2[::2, ::2] = 0
arr2[1::2, 1::2] = 0
print("-- A 8x8 matrix and filled with a checkerboard pattern --")
print(arr2)

list = np.array([10, 20, 10, 30, 20, 40, 20, 20, 10, 30, 0, 50, 10])
print("-- Unique values of list --")
print(np.unique(list))

list = np.array([6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57])
print("-- Values greater than 37 in list --")
print( list[list > 37] )

list = np.array([0, 12, 45.21, 34, 99.91])
print("-- Converted values of list of values from Centigrade to Fahrenheit --")
print( ( (9*list) + (32*5) ) / 5 )
