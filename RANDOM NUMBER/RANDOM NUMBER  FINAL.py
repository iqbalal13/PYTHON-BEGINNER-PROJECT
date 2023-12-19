import random
angka1 = input("masukkan angka: ")
if angka1 == int():
        if angka1 < 1:
            print("masukkan angka yang lebih besar")
        else:
            angka1 >12
            print("masukkan angka yang lebih kecil")

elif angka1 == str():
    print("input salah, jangan masukkan huruf !")
else:
        print("kamu salah")
random_angka = random.randint(1, 12)
guess = 0

while True:
   guess +=1
   tebak = input("masukkan angka: ")
   if tebak.isdigit():
        tebak = int(tebak)
        if tebak < 1:
                print("masukkan angka yang lebih besar")
        elif tebak >12:
                print("masukkan angka yang lebih kecil")
   else:
     print("masukkan angka, bukan huruf")
     continue
   if tebak == random_angka:
        print("benar !")
        break
   else:
        if tebak > random_angka:
            print(" kebesaran")
        else:
            tebak < random_angka
            print("kekecilan")
        
        
    
print("kamu menebak sebanyak " + str(guess) + " kali")