# Управление банковским счетом
# Напиши функцию create_account(initial_balance). Она должна возвращать две функции в виде кортежа: (deposit, withdraw).
# deposit(amount) увеличивает баланс.
# withdraw(amount) уменьшает баланс, если на счету достаточно средств (если нет — выводит предупреждение).
# Обе функции должны работать с одним и тем же внутренним балансом.

def create_account(initial_balance = 0) -> tuple:
    def deposit(amount: int) -> str:
        nonlocal initial_balance
        initial_balance += amount
        return f'Баланс: {initial_balance}'

    def withdraw(amount: int) -> str:
        nonlocal initial_balance
        if initial_balance - amount >= 0:
            initial_balance -= amount
            return f'Баланс: {initial_balance}'
        else:
            return f'Недостаточно средств'
    return deposit, withdraw

func1, func2 = create_account(100)
for operation in range(10):
    print(func1(int(input('Положить: '))))
    print(func2(int(input('Забрать: '))))