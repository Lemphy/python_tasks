# Реализуй декоратор не в виде функции, а в виде класса (используя магический метод __call__).
# Он должен подсчитывать и сохранять внутри себя количество вызовов функции.

class CountCalls:
    def __init__(self, function):
        self.counter = 0
        self.func = function

    def __call__(self, *args, **kwargs):
        self.counter += 1
        result = self.func(*args, **kwargs)
        print(f'Функция {self.func} вызвана {self.counter} раз')
        return result

def greeting():
    return 'Hello'

greeting = CountCalls(greeting)
print(greeting())