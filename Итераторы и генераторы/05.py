# «Цикличный итератор»: Создайте класс CycleIterator, который принимает список и бесконечно (или заданное число раз)
# циклически перебирает его элементы (например, [1, 2, 3] превращается в 1, 2, 3, 1, 2, 3...).

class CycleIterator:
    def __init__(self, lst: list[int], counter = None):
        self.lst = lst
        self.counter = counter
        self.cycles = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter is None:
            return self.lst
        else:
            self.cycles += 1
            if self.cycles > self.counter: raise StopIteration
            return self.lst

object1 = CycleIterator(list(range(1,11)), 5)
for i in object1:
    print(*i, sep = ', ')


