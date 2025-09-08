PetyaSpeed = int(input())
VasyaSpeed = int(input())
TolyaSpeed = int(input())

PetyaTime = 43872 / PetyaSpeed
VasyaTime = 43872 / VasyaSpeed
TolyaTime = 43872 / TolyaSpeed

if PetyaTime <= VasyaTime and PetyaTime <= TolyaTime:
    first_racer = "Петя"
    if VasyaTime <= TolyaTime:
        second_racer = "Вася"
        third_racer = "Толя"
    else:
        second_racer = "Толя"
        third_racer = "Вася"
elif VasyaTime <= PetyaTime and VasyaTime <= TolyaTime:
    first_racer = "Вася"
    if PetyaTime <= TolyaTime:
        second_racer = "Петя"
        third_racer = "Толя"
    else:
        second_racer = "Толя"
        third_racer = "Петя"
else:
    first_racer = "Толя"
    if PetyaTime <= VasyaTime:
        second_racer = "Петя"
        third_racer = "Вася"
    else:
        second_racer = "Вася"
        third_racer = "Петя"

print(f"1. {first_racer}\n2. {second_racer}\n3. {third_racer}")