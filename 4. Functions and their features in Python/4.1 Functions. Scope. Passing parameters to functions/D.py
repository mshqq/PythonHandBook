def take_small(money):
    result = []
    for i in range(len(money)):
        if money[i] < 100:
            result.append(money[i])
    return result
    

if __name__ == '__main__':
    money = [1, 5, 200, 0.5, 0.05, 10, 25, 1000, 5000, 1, 2, 100, 0.1, 5, 2000, 0.01]
    result = take_small(money)
    print(f"result = {result}")