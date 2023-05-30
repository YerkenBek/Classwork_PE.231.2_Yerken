user_in = input("your age: ")

try:
    user_age = int(user_in)
except ValueError:
    user_age = ""

if type (user_age) is int:
    if 0 < user_age < 120:
        message = "Your age seem real"
    else:
        message = "Seems you are kidding"

else:
    message = "You dont entered number"

print(message)