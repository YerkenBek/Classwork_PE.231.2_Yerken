import random
def get_random_int(min, max):
    result = random.random() * (max - min)
    result += min
    return int(result)

def game():
    user_in = input("guess number from 0 to 100: ")
    try:
        user_num = int(user_in)
    except ValueError:
        print("Only complete numbers!")
        game()
    else:
        if my_random > user_num:
            print("Bigger;)")
            game()
        elif my_random < user_num:
            print("Smaller;)")
            game()
        else:
            print("Grats!, %d!" % my_random)
            return

my_random = get_random_int(0, 100)
game()
