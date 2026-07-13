# «Случайные числа»: Напишите класс RandomIterator, который принимает low, high и count.
# Он должен выдавать count случайных целых чисел в указанном диапазоне.
import random

class RandomIterator:
    def __init__(self, low: int, high: int, count: int):
        self.low = low
        self.high = high
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        temp = [random.randint(self.low, self.high) for _ in range(self.count)]
        return temp

object1 = RandomIterator(1, 10, 5)
for i in object1:
    print(*i, sep = ', ')
