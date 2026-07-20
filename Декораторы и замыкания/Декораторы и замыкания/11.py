# Реализуй декоратор не в виде функции, а в виде класса (используя магический метод __call__).
# Он должен подсчитывать и сохранять внутри себя количество вызовов функции.

class CountCalls:
    def __init__(self):
        self.counter = 0

    def __call__(self, function):
        def wrapper():
            self.counter += 1
            temp = function()
            return (f'Результат функции: {temp}\n'
                    f'Объект {function} вызван {self.counter} раз.')
        return wrapper

deco = CountCalls() # создаем вызываемый объект

def greeting():
    return 'Hello'

greet = deco(greeting) # вызываем объект, который принимает функцию как аргумент, возвращается обертка, замкнувшая в себе ссылку на переданную функцию
print(greeting()) # вызываем обертку, где реализован счетчик и вызов функции
print(greeting())