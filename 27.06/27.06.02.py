user_in = input("list of numbers: ")
user_list  = user_in.split(",")
num_list = [int(x) for x in user_list]

for x in num_list:
    if x % 2 == 0:
        result = x * 2
    if x % 2 == 1:
        result = x - 3
print (result)
    

    

