# Умножитель на заданное число (multiplier)
# Создай функцию make_multiplier(factor).
# Она должна возвращать функцию, которая умножает любой переданный ей аргумент на factor.

def make_multiplier(factor):
    def temp(arg):
        return arg * factor
    return temp

func = make_multiplier(5)
print(func(4))