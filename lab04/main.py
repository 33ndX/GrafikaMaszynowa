from PIL import Image
import numpy as np

# ------------------- Zad 5 --------------------

def rysuj_pasy_pionowe_szare(w, h, grub,  zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (h, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = 6
    kolor_g = 4
    kolor_b = 2
    ile = int(w/grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = (kolor_r - zmiana_koloru_r) % 256
        kolor_g = (kolor_g - zmiana_koloru_g) % 256
        kolor_b = (kolor_b - zmiana_koloru_b) % 256
    return Image.fromarray(tab)

obraz6 = rysuj_pasy_pionowe_szare(200, 200, 10, 300, 200, 26,)
# print(obraz6.mode)

# ------------------- Zad 6 --------------------

def rysuj_po_skosie_szare(h, w, a, b):  # formuła zmiany wartości elemntów tablicy a*i + b*j
    t = (h, w)  # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a * i + b * j) % 256
    return Image.fromarray(tab)

kanal_alfa = np.asarray(rysuj_po_skosie_szare(200, 200, len("Pawel"), len("Milanowski")))
obraz7 = np.dstack((obraz6, kanal_alfa))
obraz7 = Image.fromarray(obraz7, mode='RGBA')

# ------------------- Zad 7 --------------------