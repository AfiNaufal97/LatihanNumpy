import numpy as np

# mengatur type data pada array di numpy
# dengan dtype
a = np.array([1, 2, 3, 4, 5], dtype = float)
print(a)

# mengalikan masing masing item dalam array dengan eksponen
b = np.array([1, 2, 3, 4, 5])
print(b**2)

# fromfunction operator
def hitung(baris,kolom):
    return kolom ** 2

print(hitung(1, 5))

hasil = np.fromfunction(hitung, (1, 5), dtype=int)
print(hasil)

# fromiterable
iterable = (x*x for x in range(5))
hasil2 = np.fromiter(iterable, dtype=int)
print(hasil2)


# multiple array dengan python
nama = [("afi", 168), ("rizal", 169), ("niko", 170)]
print(nama)

# multiple array dengan numpy
typeIni = [("nama","S255"), ("Tinggi", int)]

hasilnya = np.array(nama, dtype=typeIni)
print(hasilnya)
