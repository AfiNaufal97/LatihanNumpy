import numpy as np
import tkinter
import matplotlib.pyplot as plt

a = np.arange(0,11, 1)
print(a)

b = a*2 + 3
print(b)

# persamaan dengan grafik
# plt.plot(a, b)
# plt.show()

# lingkaran
jari2 = 5
sudut = np.linspace(0,2*np.pi,100)
print(sudut)
x2 = jari2*np.cos(sudut)
y2 = jari2*np.sin(sudut)
plt.plot(x2, y2)
plt.show()