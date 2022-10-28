# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

def greed_count(list_1, list_2):
    return 0 if len(list_1) < len(list_2) else list_1.startswith(list_2) + greed_count(list_1[1:], list_2)

list_1 = input('Введите строку в которой будем искать ')
list_2 = input('Введите строку которую будем искать ')

print(greed_count(list_1, list_2))
