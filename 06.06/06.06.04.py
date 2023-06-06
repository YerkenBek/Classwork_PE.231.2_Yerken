import random

def get_random_int(min, max):
    result = random.random() * (max - min)
    result += min
    return int(result)


num = get_random_int(5, 20)
print(num)


