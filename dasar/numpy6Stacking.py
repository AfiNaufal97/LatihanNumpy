import numpy as np

a = np.array([1, 2, 3])
b = np.array([3, 4, 5])

# hstack
# merubah menjadi satu baris
c = np.hstack([a, b])
d = np.vstack((a, b))
print(d)

# merubah element yang ukuran kolom tidak sama dengan vstack dan hstack
mZeros = np.zeros([2,3])
mOnes = np.ones([2,3])
hasil = np.vstack((mZeros, mOnes))
hasil2 = np.hstack((mZeros, mOnes))
print(hasil)
print(hasil2)

# jika ukuran baris sama dan kolom berbeda
mZeros2 = np.zeros((2,2))
mOnes2= np.ones((2,3))
# vstack dapat dilakukan karena jumlah kolom berbeda
# hasilV = np.vstack((mZeros2, mOnes2))
# print(hasilV)
# hstack bisa karena jumah kolom sama
hasilH = np.hstack((mZeros2, mOnes2))
print(hasilH)