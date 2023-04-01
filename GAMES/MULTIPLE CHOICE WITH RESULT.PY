print("let's exercise your knowledge with this multiple choice!")
score = 0
while True:
  question1 = print("1. apakah bumi bulat atau datar? ")
  choice1 = print(
           "A. datar "
           "B. segitiga "
           "C. jajar genjang "
           "D. bulat ")
  answer1 = str(input("jawab: "))
  if answer1 == "a":
   print("salah")
  elif answer1 == "b":
   print("salah")
  elif answer1 == "c":
   print("salah")
  elif answer1 == "d":
   print("benar")
   score += 20
  elif answer1 == "q":
    break
  else:
   print("input salah")


  question2 = print("2. siapakah nama presiden pertama indonesia? ")
  choice2 = print("A. dn aidit"
                 "B. jokowi "
                 "C. obama "
                 "D. sukarno ")
  answer2 = str(input("jawab: "))
  if answer2 == "a":
   print("salah")
  elif answer2 == "b":
   print("salah")
  elif answer2 == "c":
   print("salah")
  elif answer2 == "d":
   print("benar")
   score += 20
  elif answer2 == "q":
    break
  else:
   print("input salah")

  question3 = print("3. siapakah orang pertama di bulan? ")
  choice3 = print("A. yuri gagarin "
                "B. neil armstrong "
                "C. darwin "
                "D. dwakins ")
  answer3 = str(input("jawab: "))
  if answer3 == "a":
   print("salah")
  elif answer3 == "b":
   print("benar")
   score += 20
  elif answer3 == "c":
   print("salah")
  elif answer3 == "d":
   print("salah")
  elif answer3 == "q":
    break
  else:
   print("input salah")

  question4 = print("4. siapakah juara race f1 terbanyak? ")
  choice4 = print("A. hamilton "
                "B. leclerc "
                "C. maldonado "
                "D. sainz ")
  answer4 = str(input("jawab: "))
  if answer4 == "a":
   print("benar")
   score += 20
  elif answer4 == "b":
   print("salah")
  elif answer4 == "c":
   print("salah")
  elif answer4 == "d":
   print("salah")
  elif answer1 == "q":
   break
  else:
   print("input salah")

  question5 = print("5. siapakah pemenang pileg 1999 ")
  choice5 = print("A. pks "
                "B. golkar "
                "C. pdip "
                "D. psi ")
  answer5 = str(input("jawab: "))
  if answer5 == "a":
   print("salah")
   break
  elif answer5 == "b":
   print("salah")
   break
  elif answer5 == "c":
   print("benar")
   score += 20
   break
  elif answer5 == "d":
   print("salah")
   break
  elif answer1 == "q":
    break
  else:
   print("input salah")
   break
if score > 50:
    print("kamu lulus")  
elif score < 50:
    print("kamu gagal")
else:
    score = 50
    print("kamu gagal")
 

