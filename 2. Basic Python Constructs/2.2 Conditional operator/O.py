firstNumber = int(input())
secondNumber = int(input())

num1 = firstNumber // 10
num2 = firstNumber % 10
num3 = secondNumber // 10
num4 = secondNumber % 10

min_num = 9999
max_num = -9999

if num1 > max_num:
    max_num = num1
if num1 < min_num:
    min_num = num1
if num2 > max_num:
    max_num = num2
if num2 < min_num:
    min_num = num2
if num3 > max_num:
    max_num = num3
if num3 < min_num:
    min_num = num3
if num4 > max_num:
    max_num = num4
if num4 < min_num:
    min_num = num4
    
summ = num1 + num2 + num3 + num4 - max_num - min_num

if summ >= 10:
    summ %= 10    
    
print(max_num, summ, min_num, sep='')