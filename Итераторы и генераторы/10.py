# «Фильтр объектов»: Напишите класс Warehouse (Склад),
# хранящий список товаров (каждый товар — словарь или объект с атрибутами name и price).
# Реализуйте метод-генератор, который выдает только товары дороже заданной цены.

class Warehouse:

    def __init__(self):
        self.items = {'Картошка': 39,
                 'Огурцы': 53,
                 'Помидоры': 15,
                 'Зелень': 24,
                 'Бананы': 80,
                 'Персики': 43,
                      }

    def get_item(self, price):
        for k, v in self.items.items():
            if v >= price:
                yield f'{k} - {v}'

obj = Warehouse()
for i in obj.get_item(30):
    print(i)