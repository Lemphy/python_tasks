# «Простые числа»: Реализуйте класс PrimeIterator, который возвращает первые N простых чисел.
import math

class PrimeIterator:
    def __init__(self, counter: int):
        self.counter = counter
        self.value = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter:
            while True:
                for i in range(2, int(math.sqrt(self.value) + 1)):
                    if self.value % i == 0:
                        self.value += 1
                        break
                else:
                    self.counter -= 1
                    temp = self.value
                    self.value += 1
                    return temp
        else:
            raise StopIteration

object1 = PrimeIterator(10)
for i in object1:
    print(i, end = ' ')