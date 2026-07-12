# «Четные числа»: Реализуйте итератор EvenNumbers, который принимает диапазон (start, end) /
# и возвращает только четные числа из этого промежутка.

class EvenNumbers:
    def __init__(self, start, end):
        self.start = start + 1 if start % 2 != 0 else start
        self.end = end
        self.increment = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            temp = self.start
            self.start += self.increment
            return temp
        raise StopIteration

tmp = EvenNumbers(3,16)
x = iter(tmp)
while True:
    print(next(x))