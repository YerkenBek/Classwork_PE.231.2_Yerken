string = input("введите строку: ")
user_in = input("сколько раз повторить?")
repeats = int(user_in)

result = string * repeats

template = "Результат: %s"

message = template % result

print(message)
