count = int(input())
result = 0

for _ in range(count):
    counter = 0
    text = input()
    while text != "ВСЁ":
        if "зайка" in text:
            counter += 1
        text = input()
    if counter >= 1:
        result += 1
print(result)