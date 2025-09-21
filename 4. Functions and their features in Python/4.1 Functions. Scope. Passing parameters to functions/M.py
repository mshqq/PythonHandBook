unique = []


def modern_print(text):
    global unique
    if text not in unique:
        print(text)
        unique.append(text)
    else:
        return None


if __name__ == "__main__":
    modern_print("Ало!")
    modern_print("Ало!")
    modern_print("Я тебя не слышу")
    modern_print("Ало!")
    modern_print("Ало!")
    modern_print("Позвони когда сможешь")
    modern_print("Позвони когда сможешь")
    modern_print("Я тебя не слышу")