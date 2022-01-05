# Problem 2
import numpy as np
from numpy import linalg
print()

A = np.random.rand(3,3)
B = np.random.rand(3,3)

print("-- A + B --")
print(A + B)
print("-- A * B --")
print(A * B)
print("-- det(A) --")
print(linalg.det(A))
print("-- inv(B) --")
print(linalg.inv(B))
print("-- eigvals(A) --")
print(linalg.eigvals(A))