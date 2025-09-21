counter = 0
bunny_count = int(input())

for i in range(bunny_count):
    text = input()
    if "зайка" in text:
        counter += 1
print(counter)