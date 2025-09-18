a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b == 0 and c != 0:
    print("No solution")
elif a == 0:
    x = -c / b
    print(round(x, 2))
else:
    if D < 0:
        print("No solution")
    elif D == 0.0:
        x = -b / (2 * a)
        print(round(x, 2))
    else:
        x1 = (-b + D ** (1 / 2)) / (2 * a)
        x2 = (-b - D ** (1 / 2)) / (2 * a)
        if x1 > x2:
            print(round(x2, 2), round(x1, 2))
        else:
            print(round(x1, 2), round(x2, 2))