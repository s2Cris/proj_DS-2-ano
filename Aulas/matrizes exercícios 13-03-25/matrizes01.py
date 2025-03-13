import numpy as np

MAT = np.array([[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]])

SOMALINHA = []

soma = np.sum(MAT, axis=1)

SOMALINHA.append(soma)

TOTAL = np.sum(SOMALINHA)

print(MAT)
print(SOMALINHA)
print(TOTAL)
