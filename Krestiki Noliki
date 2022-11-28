import random
array = []


def create_array():
    array = []
    for i in range(3):
        array_1 = []
        for j in range(3):
            array_1.append('-')
        array.append(array_1)
    return array

def print_array(array):
    for i in range(3):
        print(" ".join(array[i]))

def chek_win(array):
    win = '-'
    for j in range(3):
        result = ''
        # print('~~~~~~~~~')
        # print(result)
        for i in range(3):
            # print('--------')
            # print(result)
            result += array[i][j]
            if result == 'XXX':
                win = 'Крестик'
            elif result == 'OOO':
                win = 'Нолик'

    for i in range(3):
        result = ''
        for j in range(3):
            result += array[i][j]
            if result == 'XXX':
                win = 'Крестик'
            elif result == 'OOO':
                win = 'Нолик'

    result = ''

    for i in range(3):
        for j in range(3):
            if i == j:
                result += array[i][j]
                # print('~~~~~~~~~')
                # print(result)
                if result == 'XXX':
                    win = 'Крестик'
                elif result == 'OOO':
                    win = 'Нолик'
    result2 = ''
    for i in range(3):
        for j in range(3):
            if i + j == 2:
                result2 += array[i][j]
                # print('~~~~~~~~~')
                # print(result)
                if result2 == 'XXX':
                    win = 'Крестик'
                elif result2 == 'OOO':
                    win = 'Нолик'

    # for i in range(3):
    #     result = ''
    #     rezalt = 'X\nX\nX\n'
    #     for j in range(3):
    #         if i == j:
    #             result += array[i][j]
    #             print(result)
    #             print('******')
    #             print(rezalt)
    #             if result == 'X\nX\nX\n':
    #                 win = 'Крестик'
    #             elif result == 'OOO':
    #                 win = 'Нолик'


    return win




table = create_array()
char = 'X'

while True:
    print_array(table)
    print(table)
    # row = int(input('Введите строку хода '))
    # line = int(input('Введите столбец хода '))
    if char == 'O':
        row = random.randint(1, 3)
        line = random.randint(1, 3)
        while table[row - 1][line - 1] == 'O' or table[row - 1][line - 1] == 'X':
            print('Комп поставил на поле которое занято ')
            row = random.randint(1, 3)
            line = random.randint(1, 3)
        print('Комп поставил нолик ')

    # table[row - 1][line - 1] = char
    if char == 'X':
        row = int(input('Введите строку хода '))
        line = int(input('Введите столбец хода '))
        while table[row - 1][line - 1] == 'O' or table[row - 1][line - 1] == 'X':
                print('Это поле занято ')
                row = int(input('Введите другую строку хода '))
                line = int(input('Введите другой столбец хода '))


    table[row - 1][line - 1] = char

    if char == 'X':
        char = 'O'
    else:
        char = 'X'

    if chek_win(table) == 'Крестик' or chek_win(table) == 'Нолик':
        print(f"Выиграл {chek_win(table)}")
        print(print_array(table))
        break


