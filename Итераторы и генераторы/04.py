# «Итератор Фибоначчи»: Реализуйте класс Fibonacci,
# который генерирует первые N чисел Фибоначчи.

class Fibonacci:
    def __init__(self, max_ = 1):
        self.counter = 0
        self.max_ = max_
        self.x = 0
        self.y = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= self.max_:
            self.counter += 1
            temp = self.x
            self.x, self.y = self.y, self.x + self.y
            return temp
        else:
            raise StopIteration

object1 = Fibonacci(30)
for i in object1:
    print(i)
