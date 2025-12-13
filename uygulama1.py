import string

# Dosyayı okuma
try:
    with open("uygulama1.txt", "r", encoding="utf-8") as f:
        text = f.read()
        print(text)
except:
    print("Dosya bulunamadi")

text_yeni =text.split()
metin=[]

#Harfleri küçük harf yapma
for i in text_yeni:
    metin.append(i.lower())
    
# Noktalama işaretlerini kaldırma    
for i in metin:
    i.replace(string.punctuation,' ')

print(metin)



