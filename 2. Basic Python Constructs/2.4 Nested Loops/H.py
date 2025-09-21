size = int(input())
max_counter = 0
max_name = ""

for i in range(size):
    counter = 0
    name = input()
    number = int(input())
    while number > 0:
        digit = number % 10
        counter += digit
        number //= 10
    if counter >= max_counter:
        max_counter = counter
        max_name = name
print(max_name)