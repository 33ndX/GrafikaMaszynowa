import sys
from PIL import Image
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

obrazek = Image.open("inicjaly.bmp")

# ------------------- Zad 2 --------------------
# print("---------- informacje o obrazie")
# print("tryb:", obrazek.mode)
# print("format:", obrazek.format)
# print("rozmiar:", obrazek.size)
#obrazek.show()

# ------------------- Zad 3 --------------------
dane_obrazek = np.asarray(obrazek)
#Zapisanie do TXT
#np.savetxt("inicjaly.txt", dane_obrazek, fmt="%2d")

# ------------------- Zad 4 --------------------
pixel1 = obrazek.getpixel((50,30))
pixel2 = obrazek.getpixel((90,40))
pixel3 = obrazek.getpixel((90,0))

# print("Pixel 1: ", pixel1)
# print("Pixel 2: ", pixel2)
# print("Pixel 3: ", pixel3)

# ------------------- Zad 5 --------------------
# tablica_bool = np.loadtxt("inicjaly.txt", dtype=np.bool_)
# print("typ danych tablicy t1: ", tablica_bool.dtype)  # typ danych przechowywanych w tablicy
# print("rozmiar tablicy t1: ", tablica_bool.shape)  # rozmiar tablicy - warto porównac z rozmiarami obrazka
# print("wymiar tablicy t1: ", tablica_bool.ndim)  # wymiar mówi czy to jest talica 1D, 2d, 3D ...

# ------------------- Zad 6 --------------------
tablica_uint8 = np.loadtxt("inicjaly.txt", dtype=np.uint8)
print("typ danych tablicy t1: ", tablica_uint8.dtype)
print("rozmiar tablicy t1: ", tablica_uint8.shape)
print("wymiar tablicy t1: ", tablica_uint8.ndim)





