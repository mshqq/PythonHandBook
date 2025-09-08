number = int(input())

n1 = number // 1000
n2 = number // 100 % 10
n3 = number % 100 // 10
n4 = number % 10

if n1 == n4 and n3 == n2:
    print("YES")
else:
    print("NO")