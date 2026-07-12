# «Шагомер»: Напишите класс StepIterator, аналогичный встроенной функции range(),
# но принимающий три аргумента: start, stop и step.

class StepIterator:
    def __init__(self, *arg): # получаем кортеж и смотрим сколько в нем элементов, от этого решаем приоритет аргументов
        if len(arg) == 1:
            self.start = 0
            self.stop = arg[0]
            self.step = 1
        elif len(arg) == 2:
            self.start = arg[0]
            self.stop = arg[1]
            self.step = 1
        elif len(arg) == 3:
            self.start = arg[0]
            self.stop = arg[1]
            self.step = arg[2]
        else: print('1-3 arguments only!')

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            temp = self.start
            self.start += self.step
            return temp
        raise StopIteration

object1 = StepIterator(3,8,2)
for i in object1:
    print(i)