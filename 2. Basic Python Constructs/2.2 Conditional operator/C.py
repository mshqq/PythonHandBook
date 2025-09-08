PetyaSpeed = int(input())
VasyaSpeed = int(input())
TolyaSpeed = int(input())

PetyaTime = 43872 / PetyaSpeed
VasyaTime = 43872 / VasyaSpeed
TolyaTime = 43872 / TolyaSpeed

if PetyaTime < VasyaTime:
    if PetyaTime < TolyaTime:
        print("Петя")
    else:
        print("Толя")
else:
    if VasyaTime < TolyaTime:
        print("Вася")
    else:
        print("Толя")
