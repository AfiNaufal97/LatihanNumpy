import numpy as np

a = np.array([(2, 3), (1, 2)])
b = np.array([23, 14])

print(a)
print(b)

# menghitung martrix dengan dot
a_inv = np.linalg.inv(a)
hasil1 = np.dot(a_inv, b)
print(hasil1)

# menghitung invers dengan solve
# saat menggunakan solve tidak perlu melakukan invers terlebih dahulu
hasil2 = np.linalg.solve(a, b)
print(hasil2)