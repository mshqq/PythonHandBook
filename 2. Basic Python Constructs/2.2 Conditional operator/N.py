number = int(input())

n1 = number // 100
n2 = number // 10 % 10
n3 = number % 100 % 10

min_num = 9999
max_num = -9999

if n1 != 0:
    n = n1 * 10 + n2
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n
    n = n1 * 10 + n3
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n
if n2 != 0:
    n = n2 * 10 + n1
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n
    n = n2 * 10 + n3
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n
if n3 != 0:
    n = n3 * 10 + n2
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n
    n = n3 * 10 + n1
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n
        
print(min_num, max_num)