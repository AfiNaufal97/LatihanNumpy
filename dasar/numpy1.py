# numeric
import numpy as np

# array
a = np.array([1, 2, 3, 4, 5])
print(a)

# arange (aray dengan range)
# arange(nilai awal, nilai akhir-1, increment)
b = np.arange(1, 10, 1)
print(b)

# linespase
# membagi menjadi sama rata
c = np.linspace(1, 10, 4)
print(c)

# array dalam element
d = np.array([(1, 2, 3, 4, 5), (6, 7, 8, 9, 10)])
print(d)

# zeros
e = np.zeros([5,5])
print(e)

# ones
f = np.ones([5, 5])
print(f)

# matrix identitas
g = np.identity(5)
print(g)
h = np.eye(5)
print(h)