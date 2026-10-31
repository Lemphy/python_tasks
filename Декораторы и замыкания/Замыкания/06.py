# Шагомер
# Создай функцию make_tracker(start_steps=0). Возвращаемая функция при каждом вызове без аргументов
# должна увеличивать количество шагов на 100 и возвращать текущее значение. Если передать число в качестве аргумента,
# оно должно прибавляться вместо дефолтных 100.
from typing import Callable

def make_tracker(start_steps: int = 0) -> Callable:
    def wrapper(value = 100):
        nonlocal start_steps
        start_steps += value
        return start_steps
    return wrapper

temp1 = make_tracker()
temp2 = make_tracker(500)
for i in range(3):
    print(temp1(), temp2())