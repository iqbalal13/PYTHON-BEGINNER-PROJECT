print("selamat datang di petualangan")

pemerintah = 0
rakyat = 0
while True:
 question = str(input("jalan ke kanan / ke kiri? : "))

 if question == "kiri":
   question = str(input("anda dimminta menghadap presiden "))
   if question == "yes":
    print("anda diculik")
    question = str(input("anda diculik, ikut / kabur? : "))
    if question == "kabur":
     print("anda selamat dan misi berhasil")
     rakyat += 1

    elif question == "ikut":
      print("game over")
      pemerintah += 1
      
    elif question == "no":
     print("tembak di tempat, game over")
     pemerintah += 1

   else:
    print("input salah")

 elif question == "kanan":
     print("anda diminta jadi peserta demo ")
     question = str(input("mau ikut atau tidak: "))
     if question == "tidak":
        print("game over")
     else:
        question == "iya"
        print("anda selamat dunia akhirat")
 else:
  question == "q"
  print("kamu keluar dari game")  
  break
if pemerintah > rakyat:
       print("rezim menang " + str(pemerintah) +" kali")
elif pemerintah < rakyat:
       print("rezim tumbang, rakyat menang" + str(rakyat +" kali"))
elif rakyat > pemerintah:
       print("rezim tumbang, rakyat menang" + str(rakyat +" kali"))
elif rakyat < pemerintah:
       print("rezim menang" + str(rakyat +" kali"))
else:
       pemerintah == rakyat
       print("hasil seri")