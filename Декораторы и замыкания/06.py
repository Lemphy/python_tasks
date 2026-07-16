# Шагомер
# Создай функцию make_tracker(start_steps=0). Возвращаемая функция при каждом вызове без аргументов
# должна увеличивать количество шагов на 100 и возвращать текущее значение. Если передать число в качестве аргумента,
# оно должно прибавляться вместо дефолтных 100.

def make_tracker(start_steps = 0):
    def temp(increment = 100):
        nonlocal start_steps
        start_steps += increment
        return start_steps
    return temp

func = make_tracker()
for i in range(3):
    print(func())