string = input()
counter = 0
while string != "Приехали!":
    if "зайка" in string:
        counter += 1
    string = input()
print(counter)