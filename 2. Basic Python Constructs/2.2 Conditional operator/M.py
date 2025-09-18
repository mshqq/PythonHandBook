num1 = int(input())
num2 = int(input())
num3 = int(input())

num1_1 = num1 // 10
num1_2 = num1 % 10
num2_1 = num2 // 10
num2_2 = num2 % 10
num3_1 = num3 // 10
num3_2 = num3 % 10

if (num1_1 == num2_1) and (num1_1 == num3_1):
    print(num1_1)
elif (num1_2 == num2_2) and (num1_2 == num3_2):
    print(num1_2)