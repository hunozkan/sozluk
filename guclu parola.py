import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parola = ""
uzunluk = int(input('Lütfen uzunluğu giriniz: '))

for i in range(uzunluk):
    parola += random.choice(karakterler)
print(parola)
