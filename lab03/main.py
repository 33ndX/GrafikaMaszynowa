from PIL import Image
import numpy as np

# ------------------- Zad 1 --------------------

def rysuj_ramki_szare(w, h, grub):
    tab = np.zeros((h, w), dtype=np.uint8)
    ile_ramek = min(w, h) // (2 * grub)
    for i in range(ile_ramek):
        kolor = 200 if i % 2 == 0 else 255
        y1, y2 = i * grub, h - i * grub
        x1, x2 = i * grub, w - i * grub
        tab[y1:y2, x1:x1 + grub] = kolor
        tab[y1:y2, x2 - grub:x2] = kolor
        tab[y1:y1 + grub, x1:x2] = kolor
        tab[y2 - grub:y2, x1:x2] = kolor
    return Image.fromarray(tab)
# ramki = rysuj_ramki_szare(200, 200, 10)
# ramki.show()

def rysuj_pasy_pionowe_szare(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w/grub)
    for k in range(ile):
        for g in range(grub):
            j = k * grub + g
            for i in range(h):
                tab[i, j] = (k + 10) % 256
    return Image.fromarray(tab)

# pionowe = rysuj_pasy_pionowe_szare(246, 100, 1)
# pionowe.show()

# ------------------- Zad 2 --------------------

def negatyw(obraz):
    tablica_obrazu = np.asarray(obraz)
    tablica_negatyw = np.copy(tablica_obrazu)
    match obraz.mode:
        case '1':
            tablica_negatyw = ~tablica_obrazu
        case 'L':
            tablica_negatyw = 255 - tablica_obrazu
        case 'RGB':
            tablica_negatyw = 255 - tablica_obrazu
        case _:
            return None
    return Image.fromarray(tablica_negatyw)

gwiazdka = Image.open("gwiazdka.bmp")
# negatyw_gwiazdka = negatyw(gwiazdka)
# negatyw_gwiazdka.show()

def rysuj_ramke_kolor(w, h, grub, kolor_ramki, kolor_tla):  # kolor_ramki, kolor podajemy w postaci [r, g, b]
    t = (h, w, 3)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)  # deklaracja tablicy
    tab[:] = kolor_ramki  # wypełnienie tablicy kolorem kolor_ramki
    tab[grub:h - grub, grub:w - grub, 0] = kolor_tla[0]  # wartości kanału R
    tab[grub:h - grub, grub:w - grub, 1] = kolor_tla[1]  # wartości kanału G
    tab[grub:h - grub, grub:w - grub, 2] = kolor_tla[2]  # wartości kanału B
    # tab[grub:h - grub, grub:w - grub] = kolor_tla # wersja równoważna
    return Image.fromarray(tab)

# ramki_kolorowe = rysuj_ramke_kolor(200, 220, len('Paweł'), len('Milanowski'), len('Pawel') * (-1))
# negatyw2 = negatyw(ramki_kolorowe)
# negatyw2.show()

def rysuj_po_skosie_szare(h, w, a, b):  # formuła zmiany wartości elemntów tablicy a*i + b*j
    t = (h, w)  # rysuje kwadratowy obraz
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            tab[i, j] = (a * i + b * j) % 256
    return Image.fromarray(tab)


# po_skosie_szare_2c = rysuj_po_skosie_szare(100, 300, len('Paweł'), len('Milanowski'))
# negatyw3 = negatyw(po_skosie_szare_2c)
# negatyw3.show()


# ------------------- Zad 3 --------------------

def koloruj_w_paski(obraz, grub, kolory=None):
    if kolory is None:
        kolory = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    tab = np.asarray(obraz).astype(np.uint8)
    h, w = tab.shape
    tab_nowego_obrazu = np.ones((h, w, 3), dtype=np.uint8) * 255
    ile = int(h / grub) + 1
    for i in range(ile):
        kolor = kolory[i % len(kolory)]
        for g in range(grub):
            wiersze = i * grub + g
            if wiersze >= h:
                break
            maska = (tab[wiersze, :] == 0)
            for c in range(3):
                tab_nowego_obrazu[wiersze, maska, c] = kolor[c]
    return Image.fromarray(tab_nowego_obrazu)

koloruj_w_paski(gwiazdka, 5).show()

# ------------------- Zad 4 --------------------
"""
Przy 328 i -24 wyskakuje komuikat, że wartość jest poza zakresem. Typ uint8 oznacza liczbe bez znaku (dodatnią), całkowitą 8 bitową, więc jej zakres to 0-255.
"""