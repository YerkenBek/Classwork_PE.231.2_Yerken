user_in = input("add buy cost: ")
cost = int(user_in)

if cost < 1000:
    print("скидок нет.")
if cost < 2000:
    print("скидка 2%.")
if cost < 5000:
    print("скидка 5%.")
else:
    print("скидка 10%.")
print("конец")
