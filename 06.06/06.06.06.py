import random
def get_random_int(min, max):
    result = random.random() * (max - min)
    result += min
    return int(result)

def game(my_random):
    user_in = input("guess number from 0 to 100: ")
    try:
        user_num = int(user_in)
    except ValueError:
        print("Only complete numbers!")
        game(my_random)
    else:
        if my_random > user_num:
            print("Bigger;)")
            game(my_random)
        elif my_random < user_num:
            print("Smaller;)")
            game(my_random)
        else:
            print("Grats!, %d!" % my_random)
            return

num = get_random_int(0, 100)
game(num)