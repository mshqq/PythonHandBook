max_number = int(input())

row = 1
col = 1
number = 1

for i in range(number, max_number + 1):
    while col <= row and number <= max_number:
        print(number, end=" ")
        col += 1
        number += 1
    print()
    col = 1
    row += 1