a = int(input())
b = int(input())

old_a = a
old_b = b

while b != 0:
    c = a
    a = b
    b = c % b
    
nod = a
nok = (old_a * old_b) // nod
print(nok)