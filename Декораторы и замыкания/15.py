# Угадай число (счетчик попыток внутри)
# Напиши функцию guess_game(secret_number). Она возвращает функцию, которая принимает вариант ответа от пользователя.
# Внутренняя функция должна сравнивать ответ с secret_number, выводить "Больше", "Меньше" или "Угадал!",
# а также хранить внутри и выводить при каждой попытке её порядковый номер.

def guess_game(secret_number: int):
    counter = 0
    def temp(answer: int) -> str:
        nonlocal counter
        if answer < secret_number:
            counter += 1
            return 'Больше!'
        elif answer > secret_number:
            counter += 1
            return 'Меньше!'
        else:
            counter += 1
            return f'Угадал за {counter} попыток.'
    return temp

func = guess_game(8)
value = func(int(input('Value: ')))
print(value)
while 'Угадал за' not in value:
    value = func(int(input('Value: ')))
    print(value)