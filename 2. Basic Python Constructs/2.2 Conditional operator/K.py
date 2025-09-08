# Согласно одному древнему поверью, трёхзначное число считается красивым, если сумма его минимальной и максимальной цифр равна оставшейся цифре умноженной на 2.

# Напишите программу, которая проверяет, является ли число красивым.

# Формат ввода
# Одно трёхзначное число

# Формат вывода
# YES — если число красивое, иначе — NO

code = int(input())

num1 = code // 100
num2 = code % 100 // 10
num3 = code % 10

if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3
    
if num1 <= num2 and num1 <= num3:
    min_num = num1
elif num2 <= num1 and num2 <= num3:
    min_num = num2
else:
    min_num = num3
    
mid_num = num1 + num2 + num3 - max_num - min_num

if max_num + min_num == mid_num * 2:
    print("YES")
else:
    print("NO")