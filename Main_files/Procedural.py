from Words_convert import value_list, keys_list, words_json

chars = ['-'] * 33
i = -1
for char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
    i += 1
    chars[i] = char

# -----------Рандом число-----------------------------
a = 1664525
c = 1013904223
m = 2 ** 32

min_value = 0

# Максимальное значение - последнее число в списке ключей или значений
len_keys_list = 0
for _ in keys_list:
    len_keys_list += 1

max_value = len_keys_list - 1
seed = 12 ** 17
# ----------------------------------------------
was_use = []

# Начальное оформление и ПРОМТ
print('-------------------------------------------------')
print('КОМПЬЮТЕР ЗАГАДЫВАЕТ СЛОВО')
print('УГАДЫВАЕТЕ БУКВУ ЗА БУКВОЙ, ОТКРЫВАЯ ИХ КАРТОЧКИ')
print('-------------------------------------------------')
print('Загадываем слово? (y)')
print('>>> ', end='')
answer = input()

while answer in 'yY':
    # Оформление
    print('\n' * 50)
    print('-------------------------------------------------')
    print('КОМПЬЮТЕР ЗАГАДАЛ СЛОВО:')

    # Выбираем случайное число не выбранное ранее
    retry = True
    random_num_result = -1
    while retry:
        num = (a * seed + c) % m
        random_num_result = min_value + (num % (max_value - min_value + 1))
        seed += 1
        if random_num_result not in was_use:
            retry = False
            was_use += [random_num_result]

    # Находим по числу слово и его объяснение в списках
    key_select = None
    value_select = None
    i = -1
    j = -1
    for key in keys_list:
        i += 1
        if i == random_num_result:
            key_select = key
    for value in value_list:
        j += 1
        if j == random_num_result:
            value_select = value

    # Помещаем выбранное слово в массив по буквам
    len_key_select = 0
    for char in key_select:
        len_key_select += 1

    word = [None] * len_key_select
    i = -1
    for char in key_select:
        i += 1
        word[i] = char

    # ДЕКОР + ПРОМТ
    print('\n')
    print('-------------------------------------------------')
    print('Загадываем слово дальше? (y)')
    print('>>> ', end='')
    answer = input()

# print('▒▒ ▒▒ ▒▒ ▒▒')
