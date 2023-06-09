
user_begin = input("num from 1 to 100: ")
user_end = input("num from 1 to 100: ")

try:
    begin = int(user_begin)
    end = int(user_end)
except ValueError:
    begin = end = None

if begin is None or end is None:
    print("need an complete number")
else:
    x = begin
    while x < end:
        x += 4
        print(x)