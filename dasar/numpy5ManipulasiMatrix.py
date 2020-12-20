import numpy as np

# trasnpose
# merubah ukuran matrix
a = np.array(([1, 2, 3], [4, 5, 6]))
print("ukuran matrix = ", a.shape)
print("sebelum transpose : \n", a)
print("hasil transpose : \n", a.transpose())

# revel membuat matrix menjadi hanya sebaris
print("ravel : ")
print(a.ravel())

# reshape
# seperti transpose hanya saja berbedar penempatan dengan transpose
print("reshape : ")
print(a.reshape(3, 2))
print(a.shape)

# resize, sperti rezie hanya saja merubah ukuran asli var a
a.resize(3, 2)
print(a)
print(a.shape)