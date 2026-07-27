import contextlib
import time

@contextlib.contextmanager
def timer(name):
    print('Вход в блок enter')
    start = time.time()
    yield 'Ставлю на паузу..'
    print('Вход в блок exit')
    end = time.time() - start
    print(f'[{timer.__name__.capitalize()}] {name} {end} секунд.')
    return None

with timer('Загрузка данных'):
    print('Выполнение тела менеджера')
    temp = sum(i for i in range(1_000_000))