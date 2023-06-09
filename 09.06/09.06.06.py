
user_in = input("num from 1 to 100: ")

try:
    user_num = int(user_in)
except ValueError:
    user_num = None

if user_num is None:
    print("need an complete number")
else:
    for x in range(1, 100):
        if x% user_num == 0:
            print(x)
