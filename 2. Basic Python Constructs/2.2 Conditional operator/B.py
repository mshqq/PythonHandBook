PetyaSpeed = int(input())
VasyaSpeed = int(input())

PetyaTime = 43872 / PetyaSpeed
VasyaTime = 43872 / VasyaSpeed

if PetyaTime < VasyaTime:
    print("Петя")
else:
    print("Вася")