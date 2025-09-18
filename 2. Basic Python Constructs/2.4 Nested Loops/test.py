while (text := input("Введите строку (СТОП для остановки): ")) != "СТОП":
    if text == "ignore_else":
        break
else:
    print("Цикл завершён")
