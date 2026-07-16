# Поиск подстроки
# Создать функцию make_searcher(query, case_sensitive=True). Она возвращает функцию,
# которая принимает текст и проверяет, содержится ли в нем query. Параметр case_sensitive определяет,
# нужно ли учитывать регистр символов при поиске.

def make_searcher(query: str, case_sensitive: bool = True):
    def temp(arg: str):
        if case_sensitive:
            return True if query in arg else False
        else:
            return True if query.lower() in arg.lower() else False
    return temp

func = make_searcher('абв')
print(func('АБВГвыфдж'))