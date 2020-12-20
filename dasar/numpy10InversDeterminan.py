import numpy as np

a = np.array([(1, -1), (1, 1)])
print(a)

# invers matrix
a_inv = np.linalg.inv(a)
print(a_inv)

print(np.dot(a, a_inv)) 

# determinan matrix
print(np.linalg.det(a))
print(np.linalg.det(a_inv))