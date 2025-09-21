n = int(input())
m = int(input())

max_number = m * n
width = 0
while max_number:
    width += 1
    max_number //= 10

for row in range(0, n):
    for col in range(0, m):
        number = row * m + col + 1
        print(f"{number:>{width}}", end=" ")
    print()