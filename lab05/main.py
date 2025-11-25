from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
import random

# ------------------- Zad 1 --------------------


# ------------------- Zad 1A --------------------
im = Image.open('img.png')
def statystyki(image):
    s = stat.Stat(image)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("rms ", s.rms)  # pierwiastek średniokwadratowy
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe
    print()

# statystyki(im)

def rysuj_histogram_RGB(obraz, title):
    hist = obraz.histogram()
    plt.title(title)
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.show()


def rysuj_histogram_L(obraz, title):
    hist = obraz.histogram()
    plt.title(title)
    plt.bar(range(256), hist[:])
    plt.show()

r, g, b = im.split()

# rgb_h = rysuj_histogram_RGB(im, 'rgb')
# rh = rysuj_histogram_L(r, 'r')
# gh = rysuj_histogram_L(g, 'g')
# bh = rysuj_histogram_L(b, 'b')




# ------------------- Zad 1B --------------------
def zlicz_piksele(obraz, kolor):
    ile = 0
    kolor = np.array(kolor)
    arr = np.array(obraz, dtype=np.uint8)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if (arr[i][j] == kolor).all():
                ile += 1
    return ile

# print("r:", zlicz_piksele(r, 155))
# print("g:", zlicz_piksele(g, 155))
# print("b:", zlicz_piksele(b, 155))

# ------------------- Zad 1C --------------------

# print("Ilość pikseli [155, 155, 155]", zlicz_piksele(im, [155, 155, 155]))

# ------------------- Zad 2 --------------------

im.save('img.jpg', "JPEG")
im_jpg = Image.open('img.jpg')

# ------------------- Zad 2A --------------------
# print("Statystki PNG:")
# statystyki(im)
#
# print("Statystki JPG:")
# statystyki(im_jpg)

'''
 Obrazy się różnią, ponieważ format JPG stosuje kompresję stratną:
 - Uśrednia sąsiadujące piksele, by zmniejszyć ilość danych
 - W efekcie spada kontrast (mniejsze stddev)
 - Występują drobne zmiany kolorów i zniekształcenia (artefakty)
'''

# ------------------- Zad 2B --------------------

diff = ImageChops.difference(im, im_jpg)
# statystyki(diff)
diff.save("roznica.png")

'''
-Różnice maksymalne nie przekraczają odpowiednio około 50–70 poziomów dla każdego kanału. 
To oznacza, że największe zmiany po kompresji JPEG występują lokalnie
- Mediany różnic są niskie (około 1–2), co pokazuje, 
że dla większości pikseli zmiany są minimalne. 
-Również wartości RMS są niskie, więc różnice mają
Odchylenia standardowe są niewielkie, ale niezerowe to wskazuje, 
że kompresja JPEG nie działa równomiernie: 
jedne piksele są praktycznie nienaruszone, a inne zmieniają się bardziej.
'''

# ------------------- Zad 2C --------------------

im_jpg.save("img2.jpg", "JPEG")
im_jpg2 = Image.open("img2.jpg")

im_jpg2.save("img3.jpg", "JPEG")
im_jpg3 = Image.open("img3.jpg")

# print("drugi raz".upper())
# statystyki(im_jpg2)
# print("trzeci raz".upper())
# statystyki(im_jpg3)

'''
 Każdy kolejny zapis JPG kumuluje pogarsza jakość:
 - Kolory stają się coraz bardziej „brudne” lub wyblakłe
 - Kontrast maleje (stddev spada)
 - Artefakty kompresji (plamki, pasy) są coraz bardziej widoczne
 - Obraz traci szczegóły, zwłaszcza w jednolitych obszarach
 '''

# ------------------- Zad 3 --------------------

# ------------------- Zad 3A i 3B --------------------

t = np.asarray(im)
t_r = t[:, :, 0]
t_g = t[:, :, 1]
t_b = t[:, :, 2]
im_r = Image.fromarray(t_r)
im_g = Image.fromarray(t_g)
im_b = Image.fromarray(t_b)
im_r.save("im_r.png")
im_g.save("im_g.png")
im_b.save("im_b.png")


im1 = Image.merge("RGB", (im_r, im_g, im_b))
diff = ImageChops.difference(im, im1)
# diff.save("diff.png")
# ------------------- Zad 3C --------------------

# plt.figure(figsize=(15, 5))
# plt.subplot(1, 3, 1)
# plt.imshow(im)
# plt.title("Oryginał (im)")
# plt.axis("off")
# plt.subplot(1, 3, 2)
# plt.imshow(im1)
# plt.title("Scalony obraz (im1)")
# plt.axis("off")
# plt.subplot(1, 3, 3)
# plt.imshow(diff)
# plt.title("Różnica (im - im1)")
# plt.axis("off")
# plt.tight_layout()
# plt.savefig("fig1.png")
# plt.show()

# ------------------- Zad 3D --------------------

# statystyki(diff)

"""
Nie widać różnic, róznica jest czarna. 
Wszystkie statystki w różnicy mają wartość 0.
"""

# ------------------- Zad 4 --------------------

# ------------------- Zad 4A --------------------
def mieszaj_kanaly(obraz):
    r, g, b = obraz.split()
    nr = Image.fromarray(255 - np.array(r, dtype=np.uint8))
    ng = Image.fromarray(255 - np.array(g, dtype=np.uint8))
    nb = Image.fromarray(255 - np.array(b, dtype=np.uint8))

    kanaly = [r, g, b, nr, ng, nb]
    etykiety = ['r', 'g', 'b', 'nr', 'ng', 'nb']
    wybrane = random.choices(kanaly, k=3)
    mix = Image.merge('RGB', wybrane)
    wybrane_etykiety = [etykiety[kanaly.index(k)] for k in wybrane]
    return mix

# mix = mieszaj_kanaly(im)
# mix.show()
# mix.save('mix.png', 'PNG')
mix = Image.open('mix.png')

# ------------------- Zad 4B --------------------

def rozpoznaj_mix(obraz, mix):
    r, g, b = obraz.split()
    nr = Image.fromarray(255 - np.array(r, dtype=np.uint8))
    ng = Image.fromarray(255 - np.array(g, dtype=np.uint8))
    nb = Image.fromarray(255 - np.array(b, dtype=np.uint8))

    oryginalne_kanaly = [r, g, b, nr, ng, nb]
    nazwy_kanalow = ["R", "G", "B", "negatyw R", "negatyw G", "negatyw B"]
    wynik = []

    for mix_kanal in mix.split():
        for nazwa, k in zip(nazwy_kanalow, oryginalne_kanaly):
            if np.all(np.array(mix_kanal) == np.array(k)):
                wynik.append(nazwa)
                break
    print('Rozpoznano:')
    print(f'R -> {wynik[0]}')
    print(f'G -> {wynik[1]}')
    print(f'B -> {wynik[2]}')

# rozpoznaj_mix(im, mix)

# ------------------- Zad 5 --------------------

imb = Image.open('beksinski1.png')
print(imb.mode)
r, g, b = imb.split()

'''
Bo obraz "beksinski1.png" jest w trybie RGBA
'''