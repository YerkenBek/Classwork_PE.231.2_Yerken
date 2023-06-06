def factor(num):
    if num == 1:
        return 1
    return num * factor(num-1)
result = factor(99)
print(result)