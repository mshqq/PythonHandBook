count_orange = int(input())
print("А Б В")
for a in range(1, count_orange):
    for b in range(1, count_orange):
        for c in range(1, count_orange):
            if (a + b + c == count_orange):
                print(a, b, c)