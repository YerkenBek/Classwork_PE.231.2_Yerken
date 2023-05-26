from re import template


user_in1 = input("enter first number: ")
user_in2 = input("enter second number: ")

try:
    num1 = float(user_in1)
    num2 = float(user_in2)
except ValueError as my_error:
    message = "You entered wrong data"
else:
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    message = template % (sum, sub, mul, div)

print(message)