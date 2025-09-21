number = int(input())
old_number = number
reversed_number = 0

while (number > 0):
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
if (old_number == reversed_number):
    print("YES")
else:
    print("NO")