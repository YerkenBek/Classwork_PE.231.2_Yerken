num = 2 + 2 * 2

if num < 6:
    print("wrong")
else:
    print("more or equal")

while num < 6:
    user_in = input("")
    if num == 6:
        break
    print("correct,", user_in)
else:
    print("more or equal")

print("the end")