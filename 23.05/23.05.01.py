user_in = input("Your salary is: ")
salary = int(user_in)

user_in = input("Credit payment per month: ")
credit = int(user_in)

user_in = input("utilities bill per month: ")
utility  = int(user_in)

result = salary - credit - utility

print("Your remains:", result)
