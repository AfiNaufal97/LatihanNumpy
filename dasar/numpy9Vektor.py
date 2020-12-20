import numpy as np

# perkalian maxtrix dengan dot
a = np.array([1, 2])
b = np.array([2, 3])
c = np.dot(a, b)
print(c)

# perkalian vektor dengan cross
a2 = np.array([1, 2, 0])
b2 = np.array([3, 4, 0])
c2 = np.cross(a2, b2)
c3 = np.cross(b2, a2)

print(c2)
print(c3)