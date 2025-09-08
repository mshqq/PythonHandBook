number = int(input())

if number == 1:
    print("NO")
else:
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            print("NO")
            break
    else:
        print("YES")