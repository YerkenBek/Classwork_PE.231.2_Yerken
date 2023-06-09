user_in = input("give the num: ")
user_num = int(user_in)

for x in range(2, user_num):
   if user_num % x == 0:
      print("the number is not simple")
      break
else:
   print(user_in)