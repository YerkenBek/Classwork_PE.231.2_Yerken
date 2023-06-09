user_in = input("give the number: ")
user_num = int(user_in)
num1 = 2
result = user_num / num1     

while result > 50:
    result /= num1
    print("try again", result)
else:
    print ("finish", result)
