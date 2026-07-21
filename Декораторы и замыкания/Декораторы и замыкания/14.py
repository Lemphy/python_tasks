# Напишите фабрику декораторов require_kwargs, которая проверяет, что при вызове функции ей были переданы определенные именованные аргументы.
# Фабрика должна принимать переменное количество строковых аргументов — имена обязательных kwargs.
# Если хотя бы один из требуемых kwargs отсутствует при вызове функции, декоратор должен вызывать TypeError.
# Если все требуемые kwargs на месте, функция должна выполниться как обычно.

def require_kwargs(*args):
    def deco(func):
        def wrapper(**kwargs):
            for arg in args:
                if arg in kwargs:
                    continue
                else:
                    raise TypeError('Недостаточно параметров')
            result = func(**kwargs)
            return result
        return wrapper
    return deco

@require_kwargs("user_id", "role")
def process_request(**kwargs):
    print(f"Обработка запроса с параметрами: {kwargs}")

process_request(user_id=10, role="admin", action="delete") # OK
process_request(user_id=11, action="read") # Вызовет TypeError