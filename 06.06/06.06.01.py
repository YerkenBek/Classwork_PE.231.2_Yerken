def get_second(hours, minutes, seconds):
    seconds_in_minutes = 60 * minutes
    seconds_in_hours = 60 * 60 * hours
    return seconds_in_hours + seconds_in_minutes + seconds

total = get_second(2, 30, 5)
print(total)
