a = int(input())
b = int(input())

while b != 0:
    c = a
    a = b
    b = c % b
print(a)