number = int(input())

i = 2
first = True

while number > 1:
    if number % i == 0:
        if first:
            print(i, end="")
            first = False
        else:
            print(" *", i, end="")
        number //= i
    else:
        i += 1