a = 1
b = 5
# a = 5
# b = -4
result = [x ** 2 for x in range(a, b + 1 if b > a else -a, 1 if a < b else -1)]
print(result)