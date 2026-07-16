# Добавление суффикса/префикса
# Напиши функцию make_encloser(prefix, suffix).
# Она возвращает функцию, которая оборачивает любую переданную строку в этот префикс и суффикс.

def make_encloser(prefix, suffix):
    def temp(string):
        return f'{prefix}{string}{suffix}'
    return temp

func = make_encloser('!!!', '...')
print(func('привет'))