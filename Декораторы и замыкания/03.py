# Линейная функция (y = kx + b). Напиши фабрику функций line_factory(k, b).
# Она должна возвращать функцию, которая принимает x и вычисляет значение линейного уравнения y = kx + b

def line_factory(k, b):
    def temp(x):
        return k * x + b
    return temp

func = line_factory(2, 4)
print(func(2))
