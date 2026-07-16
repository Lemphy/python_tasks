# Ограничитель баланса (Копилка)
# Создай функцию make_piggy_bank(limit). Возвращаемая функция принимает сумму, которую пользователь хочет положить в копилку.
# Если сумма в копилке не превышает limit, деньги добавляются, и функция возвращает текущий баланс.
# Если лимит превышен, транзакция отклоняется, баланс не увеличивается, и возвращается сообщение: "Превышен лимит копилки!".

def make_piggy_bank(limit):
    current_money = 0
    def temp(value):
        nonlocal current_money
        if current_money + value <= limit:
            current_money += value
            return f'Текущий баланс {current_money}'
        else:
            return f'Превышен лимит копилки! {current_money + value}/{limit}'
    return temp

func = make_piggy_bank(100)
next_ = 'д'
while next_.lower() == 'д':
    value = int(input('Сумма для пополнения: '))
    print(func(value = value))
    next_ = input('Продолжаем? (д,н): ')
