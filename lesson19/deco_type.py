#Реализуйте декоратор, который проверяет аргументы функции на тип данных.
# Соответствие аннотациям. Рекомендую использовать метод annotations.
# В кач-ве результата возвращаем значение bool.

def decorator (func):
    def wrapper (*args):
        annotations = list(func.__annotations__.values())
        arg = [type(i) for i in args]
        print(annotations)
        print(arg)
        return arg == annotations
    return wrapper
@decorator
def main_func(a: int, b: str, c: list):
    return f'a - {a}, b - {b}, c - {c}'

print(main_func(3, "7", [21]))