name = input()
code = int(input())
num1 = code // 100
num2 = code % 100 // 10
num3 = code % 10
print(f"Группа №{num1}.")  
print(f"{num3}. {name}.")  
print(f"Шкафчик: {code}.")  
print(f"Кроватка: {num2}.")