gen_weight = int(input())
gen_price = int(input())
first_price = int(input())
second_price = int(input())

x = (gen_weight * (first_price - gen_price)) / (first_price - second_price)
y = (gen_weight * (gen_price - second_price)) / (first_price - second_price)
print(int(y), int(x))
