# Своя база данных (Key-Value хранилище)
# Напиши функцию create_db(). Она должна возвращать словарь с тремя
# функциями: {"set": set_val, "get": get_val, "delete": del_val}.
# Все три функции работают с общим словарем внутри замыкания, позволяя записывать ключи, читать их и удалять.

def create_db():
    general_dict = {}

    def set_val(*args):
        key, value = args
        if key not in general_dict:
            general_dict[key] = value
            print('Ключ', key, 'добавлен со значением', value)
        else:
            general_dict[key] = value
            print('Ключ', key, 'обновлен со значением', value)

    def read_val(key):
        value = general_dict.get(key, 'не обнаружен')
        print(f'Ключ {key} - {value}')

    def del_val(key):
        if key in general_dict:
            del general_dict[key]
            print(f'Ключ {key} успешно удален.')
        else:
            print(f'Ключ {key} не обнаружен.')

    def check_dict_items():
        for k, v in general_dict.items():
            print(f"{k}:{v}", end = ' ')
        print()

    return {'set': set_val, 'read': read_val, 'del': del_val, 'check':check_dict_items}

operations = create_db()
next_ = 'д'
while next_ == 'д':
    print(f'Команды: \n'
          f'set - записать/обновить ключ\n'
          f'read - считать ключ\n'
          f'del - удалить ключ\n'
          f'check - проверить состояние словаря\n')
    answer = input('Ответ: ').lower()
    if answer in operations:
        if answer != 'check':
            (operations[answer])(*input('').split())
        else:
            (operations[answer])()
    else:
        print('Операция не обнаружена.')
    next_ = input('Дальше? (д/н): ')