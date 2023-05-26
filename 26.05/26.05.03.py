user_dis1 = input("dist? ")
user_tim2 = input("hours? ")

try:
    distance = int(user_dis1)
    hours = int(user_tim2)
except ValueError:
    message = "you entered wrong value"
else:
    result = distance / hours
    message = "left %s hrs" % result

print(message)

