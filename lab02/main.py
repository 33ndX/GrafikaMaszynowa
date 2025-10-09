from PIL import Image
import numpy as np


inicjaly = Image.open("inicjaly.bmp")

# print("tryb", inicjaly.mode)
# print("format", inicjaly.format)
# print("rozmiar", inicjaly.size)

# ------------------- Zad 1 --------------------
def rysuj_ramke_w_obrazie(obraz,grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(w):
            if i < grub or i > h - grub or j < grub or j > w - grub:
                tab_obraz[i][j] = 0
    tab = tab_obraz.astype(bool)
    return Image.fromarray(tab)

#rysuj_ramke_w_obrazie(inicjaly, 3).show()

# ------------------- Zad 2 --------------------


# ------------------- 1.1 --------------------

def rysuj_ramki(w,h,grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    for k in range(ile):
        for i in range(h):
            for j in range(w):
                    tab[grub:h - grub, grub:w - grub] = 0
                    tab[grub:h + grub, grub:w + grub] = 0
    tab = tab * 255
    return Image.fromarray(tab)

rysuj_ramki(100, 50, 5).show()




# ------------------- 1.2 --------------------
def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)
    ile =  int(w/grub)  # liczba pasów  o grubości grub
    for k in range(ile):  # uwaga k = 0,1,2..   bez ile
        for g in range(grub):
            j = k * grub + g  # i - indeks wiersza, j - indeks kolumny
            for i in range(h):
                tab[i, j] = k % 2  # reszta z dzielenia przez dwa
    tab = tab * 255  # alternatywny sposób uzyskania tablicy obrazu czarnobiałego ale w trybie odcieni szarości
    return Image.fromarray(tab)  # tworzy obraz

#rysuj_pasy_pionowe(100, 50, 10).show()





