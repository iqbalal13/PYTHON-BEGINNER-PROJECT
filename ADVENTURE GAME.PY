print("selamat datang di petualangan")

while True:
 question = str(input("jalan ke kanan / ke kiri? : "))

 if question == "kiri":
   question = str(input("anda dimminta menghadap presiden "))
   if question == "yes":
    print("anda diculik")
    question = str(input("anda diculik: "))
    if question == "kabur":
     print("anda selamat dan misi berhasil")
     break
    if question == "ikut":
      print("game over")
      break
    else:
      print("input salah")
   else:
    question == "no"
    print("tembak di tempat, game over")
    break

 elif question == "kanan":
     print("anda diminta jadi peserta demo ")
     question = str(input("mau ikut atau tidak: "))
     if question == "tidak":
        print("game over")
     else:
        question == "iya"
        print("anda selamat dunia akhirat")