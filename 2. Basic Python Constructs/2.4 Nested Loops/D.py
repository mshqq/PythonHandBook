count = int(input())
counter = 0
for _ in range(count):
    user_input = int(input())
    while user_input != 0:
        counter += user_input % 10
        user_input //= 10
print(counter)