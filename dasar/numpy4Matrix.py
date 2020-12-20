import numpy as np

# perkalian matrix
a = np.array(([1,2], [3, 4]))
b = np.ones([2,2])

# dot adalah perintah untuk perkalian matrix
hasil = np.dot(a, b)
print(hasil)

# cara 2 dengan receive value
hasil2 = a.dot(b)
print(hasil2)

