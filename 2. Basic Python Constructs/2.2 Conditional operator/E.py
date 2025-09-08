VasyaApples = 12
PetyaApples = 6

N = int(input())
M = int(input())

VasyaApples += M
PetyaApples += N

if VasyaApples > PetyaApples:
    print("Вася")
else:
    print("Петя")