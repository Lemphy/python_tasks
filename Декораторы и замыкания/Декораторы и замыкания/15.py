# Напишите фабрику декораторов call_limit, которая позволяет вызвать функцию не более указанного количества раз.
# Фабрика должна принимать один аргумент limit — целое число. При попытке вызвать функцию больше, чем limit раз,
# декоратор должен вызывать ValueError. Каждая задекорированная функция должна иметь свой собственный,
# независимый счетчик вызовов.
from functools import wraps

def call_limit(limit: int):
    def deco(func):
        counter = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal counter
            if counter < limit:
                result = func(*args, **kwargs)
                counter += 1
                return result
            else:
                raise ValueError (f'Функция была вызвана более {limit} раз!')
        return wrapper
    return deco

@call_limit(limit=3)
def send_email(address):
    print(f"Отправляю письмо на {address}")

send_email("a@ex.com") # OK
send_email("b@ex.com") # OK
send_email("c@ex.com") # OK
send_email("d@ex.com") # Вызовет ValueError