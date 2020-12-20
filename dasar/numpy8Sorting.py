import numpy as np

a = np.random.randn(1, 6)
print(a)

# koversi dengan dikaliakn 10 setiap item
b = a*10
print(b)

# melihat nilai max a
print("nilai max dari variable a = {}".format(a.max()))

# melihat nilai max a ada di index ke 
print("nilai max variable a ada di index ke = {}".format(a.argmax()))

# melihat nilai max a
print("nilai min dari variable a = {}".format(a.min()))

# melihat nilai max a ada di index ke 
print("nilai min variable a ada di index ke = {}".format(a.argmin()))

# urutkan dengan sort
print("urutan : {}".format(np.sort(a)))

#urutan berdasarkan index
print("urutan index : {}".format(np.argsort(a)))


# array dengan lebih dari 1 baris
c = np.random.randn(2,2)
print(c)

# max 
print(c.max())

# min
print(c.min())

# sorting
print(np.sort(c))

# sorting berdasarkan index
print(np.argsort(c))


# penggunaan order
nama = [("afi",170), ("rizal",172), ("niko",175)]

# type
nType = [("nama", "S10"), ("tinggi", int)]
arr = np.array(nama, dtype=nType)
print(arr)

# sor by nama parameter
namaHasil = np.sort(arr, order="nama")
print(namaHasil)

tinggiHasil = np.sort(arr, order="tinggi")
print(tinggiHasil)