def number_length(number):
    number = abs(number)
    return len(str(number))


if __name__ == '__main__':
    result = number_length(12345)
    print(f"result = {result}")