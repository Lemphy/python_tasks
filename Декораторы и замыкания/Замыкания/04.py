# Валидатор пароля по длине
# Создай функцию make_length_checker(min_length). Она должна возвращать функцию,
# которая принимает строку (пароль) и возвращает True, если её длина больше или равна min_length,
# и False в противном случае.

def make_length_checker(min_length: int):
    def temp(arg: str):
        return True if len(arg) >= min_length else False
    return temp

func = make_length_checker(6)
print(func('python_top'))