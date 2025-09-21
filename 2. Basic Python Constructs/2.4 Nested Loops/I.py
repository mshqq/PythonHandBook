size = int(input())


result = ''

for i in range(size):
    number = int(input())
    digit = 0
    max_digit = 0
    
    while number > 0:
        digit = number % 10
        if digit > max_digit:
            max_digit = digit
        number //= 10
    
    result = result + str(max_digit)
    
print(result)