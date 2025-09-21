__count = 0


def move(player, number):
    global __count
    if player == "Петя":
        __count += number
    elif player == "Ваня":
        __count -= number


def game_over():
    if __count > 0:
        winner = "Петя"
    elif __count < 0:
        winner = "Ваня"
    else:
        winner = "Ничья"
    return winner    

    
if __name__ == "__main__":
    move("Петя", 3)
    move("Ваня", 4)
    print(game_over())