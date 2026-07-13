# «Мигающий свет»: Создайте класс TrafficLight (Светофор).
# Метод-генератор должен поочередно выдавать строки
# "Красный", "Желтый", "Зеленый" в бесконечном цикле.

class TrafficLight:
    colors = ["Красный", "Желтый", "Зеленый"]

    def gen_color(self):
        while True:
            for i in self.colors:
                yield i

obj = TrafficLight()
for color in obj.gen_color():
    print(color)