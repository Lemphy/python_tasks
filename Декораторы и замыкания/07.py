# Электронная очередь
# Напиши функцию ticket_dispenser(). Она должна возвращать функцию,
# которая при каждом вызове выдает следующий номер билета в формате "Клиент №1", "Клиент №2" и так далее.

def ticket_dispenser():
    client = 0
    def temp():
        nonlocal client
        client += 1
        return f'Клиент №{client}'
    return temp

func = ticket_dispenser()
for i in range(10):
    print(func())