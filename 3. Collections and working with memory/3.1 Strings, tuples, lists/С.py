length = int(input())
size = int(input())
for i in range(size):
    text = input()
    if len(text) <= length:
        print(text)
    else:
        print(text[:length - 3], end="...\n")