# Написать контекстный менеджер, который замеряет время выполнения блока кода и выводит его в консоль при выходе.

from time import perf_counter

class Timer:
    def __init__(self, name):
        print('Вход в блок init')
        self._name = name
        self.start = None
        self.end = None

    def __enter__(self):
        print('Вход в блок enter')
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Вход в блок exit")
        self.end = perf_counter()
        delta = self.end = self.start
        print(f'[{self.__class__.__name__}] {self._name} {delta} секунд..')
        return True

with Timer('Загрузка данных') as tmr:
    print('Вход в основной блок')
    total = sum(i for i in range(10000000))