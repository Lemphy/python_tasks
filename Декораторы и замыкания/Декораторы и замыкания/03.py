# Напиши декоратор, который измеряет время выполнения функции и выводит его в консоль в секундах

import time

def timer(func):
    def wrapper():
        start = time.time()
        work = func()
        end = time.time()
        print(f'Время работы: {end - start:.2e}')
        return work
    return wrapper

def function():
    print("Работа функции..")

function = timer(function)
function()
