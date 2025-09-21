number = int(input())
new_number = 0
counter = 0
    
while (number > 0):
    digit = number % 10
    if (digit % 2 != 0):
        new_number = new_number + digit * (10 ** counter)
        counter += 1
    number = number // 10
print(new_number)