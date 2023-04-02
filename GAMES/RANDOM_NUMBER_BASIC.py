import random

angka = input("masukkan angka: ")

if angka.isdigit():
    angka = int(angka)
    if angka > 12:
        print("masukkan angka yang lebih kecil")
    elif angka < 1:
        print("masukkan angka yang lebih besar")
    else:
        print("angka kurang tepat")
else:
    print("input salah")
    quit()

random_angka = random.randint(1, 12)
print(random_angka)


