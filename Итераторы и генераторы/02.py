# «Квадраты массива»: Создайте класс SquareIterator, который принимает
# список чисел и возвращает их квадраты по одному за раз.

class SquareIterator:
    def __init__(self, numbers: list[int]):
        self.numbers = numbers
        self.start = 0
        self.end = len(self.numbers)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            temp = self.numbers[self.start] ** 2
            self.start += 1
            return temp
        raise StopIteration

object1 = SquareIterator(list(range(1,10)))
for i in object1:
    print(i)