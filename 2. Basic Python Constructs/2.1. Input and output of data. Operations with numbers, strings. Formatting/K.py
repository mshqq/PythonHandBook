code = int(input())
num1 = code // 1000
num2 = code // 100 % 10
num3 = code % 100 // 10
num4 = code % 10
print(num2, num1, num4, num3, sep='')