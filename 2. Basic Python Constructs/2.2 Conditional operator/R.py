a = int(input())
b = int(input())
c = int(input())

long_side = -999
short_side = 999

if a > long_side:
    long_side = a
if a < short_side:
    short_side = a
if b > long_side:
    long_side = b
if b < short_side:
    short_side = b
if c > long_side:
    long_side = c
if c < short_side:
    short_side = c
    
b = a + b + c - short_side - long_side
a = short_side
c = long_side

first_condition = a ** 2 + b ** 2 == c ** 2
second_condition = a ** 2 + b ** 2 < c ** 2

if first_condition:
    print('100%')
elif second_condition:
    print("велика")
else:
    print("крайне мала")