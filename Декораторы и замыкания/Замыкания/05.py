# Поиск подстроки
# Создать функцию make_searcher(query, case_sensitive=True). Она возвращает функцию,
# которая принимает текст и проверяет, содержится ли в нем query. Параметр case_sensitive определяет,
# нужно ли учитывать регистр символов при поиске.
from typing import Callable

def make_searcher(query: str, case_sensitive: bool = True) -> Callable:
    def wrapper(text: str) -> bool:
        return query in text if case_sensitive else query.lower() in text.lower()
    return wrapper

func = make_searcher('абв')
print(func('АБВГвыфдж'))