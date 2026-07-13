# «Алфавитный указатель»: Создайте класс AlphabetIterator, который плавно итерируется по буквам английского
# алфавита от 'A' до 'Z' (или в заданном диапазоне букв, например, от 'G' до 'P')
import string

class AlphabetIterator:
    alphas = string.ascii_uppercase

    def __init__(self, start = None, stop = None):
        if start is None and stop is None:
            self.start = start
            self.stop = stop
            self.index = 0
        else:
            self.start = self.alphas.find(str(start).upper())
            self.stop = self.alphas.find(str(stop).upper())
            self.index = self.start
        self.increment = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start is None and self.stop is None:
            if self.index < len(self.alphas):
                temp = self.alphas[self.index]
                self.index += self.increment
                return temp
            raise StopIteration
        else:
            if self.index <= self.stop:
                temp = self.alphas[self.index]
                self.index += self.increment
                return temp
            else:
                raise StopIteration

my_object = AlphabetIterator()
for char in my_object:
    print(char, end = ' ')