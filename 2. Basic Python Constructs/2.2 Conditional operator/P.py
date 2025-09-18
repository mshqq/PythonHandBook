length = 43872
speed_petya = int(input())
speed_vasya = int(input())
speed_Tolya = int(input())
time_petya = length / speed_petya
time_vasya = length / speed_vasya
time_tolya = length / speed_Tolya
if time_petya <= time_vasya and time_petya <= time_tolya:
    first_racer = "Петя"
    if time_vasya <= time_tolya:
        second_racer = "Вася"
        third_racer = "Толя"
    else:
        second_racer = "Толя"
        third_racer = "Вася"
elif time_vasya <= time_petya and time_vasya <= time_tolya:
    first_racer = "Вася"
    if time_petya <= time_tolya:
        second_racer = "Петя"
        third_racer = "Толя"
    else:
        second_racer = "Толя"
        third_racer = "Петя"
else:
    first_racer = "Толя"
    if time_petya <= time_vasya:
        second_racer = "Петя"
        third_racer = "Вася"
    else:
        second_racer = "Вася"
        third_racer = "Петя"
first_position = "I"
second_position = "II"
third_position = "III"
print(f'{"":8}{first_racer:^8}')
print(f'{second_racer:^8}')
print(f'{"":16}{third_racer:^8}')
print(f'{second_position:^8}{first_position:^8}{third_position:^8}')