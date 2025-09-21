count = int(input())
nod = int(input())

for _ in range(count - 1):
    number = int(input())
    a, b = nod, number
    while number != 0:
        a, b = b, a % b
    nod = a
print(nod)