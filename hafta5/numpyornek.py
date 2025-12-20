import numpy as np

array = np.random.randint(0,50,size=20)
print(f"Rastgele seçilen 20 deger: {array}")

np2= array/2
print(f"Degerlerin 2' ye bölümü: {np2}")

ortalama = np.mean(array)
print(f"Rastgele alinan değerlerin ortalamasi: {ortalama} ")


filtrelenmis = array[array>30] 
print(f"30 dan büyük olan değerler: {filtrelenmis}")


