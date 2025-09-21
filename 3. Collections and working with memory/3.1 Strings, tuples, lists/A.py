count = 0
size = int(input())
for i in range(size):
    text = input()
    if text[0] in "абв":
        count += 1
if (count == size):
    print("YES")
else:
    print("NO")