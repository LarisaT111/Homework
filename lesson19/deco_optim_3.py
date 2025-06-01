#Напишите декоратор, оптимизирующий работу декорируемой функции.
# Декоратор должен сохранять результат работы функции на ближайшие
# три запуска и вместо выполнения функции возвращать сохранённый результат.
# После трёх запусков функция должна вызываться вновь, а результат работы
# функции — вновь кешироваться.

from time import sleep

def decorator (func):
    count, cache = 0, {}
    def wrapper(num):
        nonlocal count
        count += 1
        if cache and count in range (1, 3):
           return cache ['cache']
        count = 0
        cache['cache'] = func(num)
        return cache ['cache']
    return wrapper
@decorator
def main_func(num):
    sleep(1)
    return num ** 2

print(main_func(2))
print(main_func(3))
print(main_func(4))
print(main_func(5))
print(main_func(6))