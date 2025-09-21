def month(number, language):
    months = {
        "ru": [
            "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
            "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
        ],
        "en": [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
    }
    if language in months and 1 <= number <= 12:
        return months[language][number - 1]
    return None


if __name__ == "__main__":
    result = month(1, "en")
    print(f"result = '{result}'")
    result = month(7, "ru")
    print(f"result = '{result}'")