import numpy as np

mat1 = np.array([[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]])
mat2 = np.array([[5,4,3,2,1], [5,4,3,2,1], [5,4,3,2,1]])

res = np.sum([mat1, mat2])

print(mat1)
print(mat2)
print(res)