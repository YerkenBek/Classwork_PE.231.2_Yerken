num = 1

if num < 10:
    print("less")
else:
    print("more or equal")

while num < 10:
    num +=1
    if num == 5:
        continue
    print("less,", num)
else:
    print("more or equal")

print("the end")