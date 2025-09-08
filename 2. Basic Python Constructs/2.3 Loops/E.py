all_price = 0
price = float(input())
while price != 0:
    if price >= 500:
        price = price - price * (10 / 100)
    all_price += price
    price = float(input())
print(all_price)