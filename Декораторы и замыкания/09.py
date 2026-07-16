# 9. Генератор уникальных ID по шаблону
# Напиши функцию id_generator(prefix). Каждому вызову возвращаемой функции присваивается уникальный ID, увеличивающийся на 1.

def id_generator(prefix: str):
    counter = 0
    def temp():
        nonlocal counter
        counter += 1
        return f'{prefix}_{counter}'
    return temp

func = id_generator('user')
for _ in range(10):
    print(func())