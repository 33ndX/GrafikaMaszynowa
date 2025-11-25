from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

# ------------------- Zad 6 --------------------


def ocen_czy_identyczne(obraz1, obraz2):
    t_obraz1 = np.asarray(obraz1)
    t_obraz2 = np.asarray(obraz2)
    roznice_pikseli = []
    if len(t_obraz1.shape) == 3:
        obraz1_w, obraz1_h, obraz1_d = t_obraz1.shape
        obraz2_w, obraz2_h, obraz2_d = t_obraz2.shape
    else:
        obraz1_w, obraz1_h = t_obraz1.shape
        obraz2_w, obraz2_h = t_obraz2.shape
    min_x = min(obraz1_w, obraz2_w)
    min_y = min(obraz1_h, obraz2_h)
    for h in range(min_y):
        for w in range(min_x):
            for k in range(3):
                if t_obraz1[w, h, k] != t_obraz2[w, h, k]:
                    roznice_pikseli.append((w, h))
    if obraz1.mode != obraz2.mode:
        print("Obrazy nie są identyczne bo, obrazy mają różne tryby")
    elif obraz1.size != obraz2.size:
        print("Obrazy nie są identyczne bo, obrazy mają różne rozmiary")
    elif obraz1.format != obraz2.format:
        print("Obrazy nie są identyczne bo, obrazy mają różne formaty")
    elif len(roznice_pikseli) > 0:
        print("Obrazy nie są identyczne bo, obrazy mają inne wartości pikseli:")
        for wsp in roznice_pikseli[:5]:
            print(wsp)
    else:
        print("Obrazy są identyczne.")


# im_beksinski = Image.open('beksinski.png')
# im_beksinski1 = Image.open('beksinski1.png')
# im_beksinski2 = Image.open('beksinski2.png')
# im_beksinski3 = Image.open('beksinski3.png')
# print('beskinski vs beksinski1')
# ocen_czy_identyczne(im_beksinski, im_beksinski1)
# print('\nbeskinski vs beksinski2')
# ocen_czy_identyczne(im_beksinski, im_beksinski2)
# print('\nbeskinski vs beksinski3')
# ocen_czy_identyczne(im_beksinski, im_beksinski3)

# ------------------- Zad 7 --------------------

def pokaz_roznice(obraz_wejsciowy):
    t_obraz = np.asarray(obraz_wejsciowy)
    if len(t_obraz.shape) == 3:
        w, h, d = t_obraz.shape
    else:
        w, h = t_obraz.shape
        d = 1
    t_wynik = np.copy(t_obraz)

    for k in range(d):
        max_wartosc_kanal = np.max(t_obraz[:, :, k])
        if max_wartosc_kanal != 0:
            t_wynik[:, :, k] = (t_obraz[:, :, k] / max_wartosc_kanal) * 255
        else:
            t_wynik[:, :, k] = 0
    obraz_wynik = Image.fromarray(t_wynik)
    return obraz_wynik

im_jpg3 = Image.open('img3.jpg')
im = Image.open('img.png')
diff = ImageChops.difference(im, im_jpg3)
diff_pokaz = pokaz_roznice(diff)

# ------------------- Zad 7C --------------------
plt.figure(figsize=(16, 12))
plt.subplot(2, 2, 1)
plt.title("Oryginalny obraz - im")
plt.axis('off')
plt.imshow(im)
plt.subplot(2, 2, 2)
plt.title("Po zapisaniu JPG  - im_jpg3")
plt.axis('off')
plt.imshow(im_jpg3)
plt.subplot(2, 2, 3)
plt.title("diff")
plt.axis('off')
plt.imshow(diff)
plt.subplot(2, 2, 4)
plt.title("pokaz_roznice(diff)")
plt.axis('off')
plt.imshow(diff_pokaz)
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')

# ------------------- Zad 8 --------------------
im = Image.open('img.png')
inicjaly = Image.open('inicjaly.bmp')
def wstaw_inicjaly(obraz_bazowy, obraz_wstawiany, m, n, kolor):
    if obraz_wstawiany.mode != '1':
        return "Nieprawidłowy tryb obrazu wstawianego"
    np_baza = np.asarray(obraz_bazowy).astype(np.int_)
    h0, w0, c = np_baza.shape
    np_wstawiany = np.asarray(obraz_wstawiany).astype(np.int_)
    h,w = np_wstawiany.shape
    n_k = min(h0, n+h)
    m_k = min(w0, m+w)
    n_p = max(0,n)
    m_p = max(0, m)
    for i in range(n_p, n_k):
        for j in range(m_p,m_k):
            if np_wstawiany[i-n, j-m] == 0:
                np_baza[i][j] = kolor
    return Image.fromarray(np_baza.astype(np.uint8))

obraz1 = wstaw_inicjaly(im, inicjaly, im.width - inicjaly.width, 0, [255, 0, 0])  # Prawy górny róg
obraz2 = wstaw_inicjaly(obraz1, inicjaly, 0, im.height - inicjaly.height, [0, 255, 0])             # Lewy dolny róg
obraz3 = wstaw_inicjaly(obraz2, inicjaly, im.width - inicjaly.width// 2, im.height // 2, [0, 0, 255])    # Środek wysokości

obraz3.save('obraz_inicjaly.png')

# ------------------- Zad 9 --------------------
def odkoduj(obraz1, obraz2):
    tab_obraz1 = np.array(obraz1)
    tab_obraz2 = np.array(obraz2)

    roznice = np.where(tab_obraz1 != tab_obraz2, 255, 0).astype(np.uint8)

    return Image.fromarray(roznice)

jesien = Image.open("jesien.jpg")
zakodowany1 = Image.open("zakodowany1.bmp")

odkod = odkoduj(jesien, zakodowany1)
odkod.save('kod2.bmp')