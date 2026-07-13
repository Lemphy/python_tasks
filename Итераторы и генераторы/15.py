# «Плоский список»: Создайте класс FlatList, который принимает вложенный список
# (например, [1, [2, 3], [4, [5]] ]). Реализуйте метод-генератор, который разворачивает его в плоскую структуру.

class FlatList:
    def __init__(self, lst: list):
        self.lst = lst

    def unpack_list(self):
        for element in self.lst:
            if isinstance(element, list):
                for el in element:
                    if isinstance(el, list):
                        for e in el:
                            yield e
                    else:
                        yield el
            else:
                yield element

obj = FlatList([1, [2, 3], [4, [5]] ])
for i in obj.unpack_list():
    print(i, end = ' ')

