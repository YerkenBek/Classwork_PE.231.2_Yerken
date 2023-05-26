user_hours = input("который час? ")
user_minutes = input("сколько минут? ")
user_seconds = input("сколько секунд? ")
seconds_total = 24 * 60 * 60

try:
    hours = int(user_hours)
    minutes = int(user_minutes)
    seconds = int(user_seconds)
except ValueError:
    message = "вы ввели не числа"
else:
    seconds_past = hours * 60 * 60 + minutes * 60 + seconds
    seconds_left = seconds_total - seconds_past
    message = "осталось %s секунд" % seconds_left

print(message)

