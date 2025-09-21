count = int(input())
counter = 0

for i in range(count):
    number = int(input())
    if number == 1:
        continue
    else:
        for i in range(2, int(number / 2) + 1):
            if number % i == 0:
                break
        else:
            counter += 1
print(counter)