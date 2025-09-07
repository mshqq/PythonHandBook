product = input()
price = int(input())
weight = int(input())
money = int(input())

summary = price * weight
change = money - summary

print(f"{'Чек':=^35}")
print(f"Товар: {product:>28}")
print(f'Цена: {f"{weight}кг * {price}руб/кг":>29}')
print(f"Итого: {summary:>25}руб")
print(f"Внесено: {money:>23}руб")
print(f"Сдача: {change:>25}руб")
print("=" * 35)