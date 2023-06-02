user_in1 = input("объем флешки в Гб? ")
user_in2 = input("размер файла в Мб? ")   
mbtotal = 1024

try:
    total = int(user_in1)
    files = int(user_in2)

except ValueError:
    message = "not correct"
else:
    copysize = mbtotal - user_in2
    message = "Осталось %s копии" % copysize

print(message)
