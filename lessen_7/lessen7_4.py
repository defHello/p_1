import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        end = end_time - start_time
        print(f'Старт {start_time} сек')
        print(f'Конец {end_time} сек')
        print(f'Время выполнения{end} сек')
        return result
    return wrapper

@time_decorator
def cickl(x, y):
    return x * y

x, y = 25, 6
print(cickl(x,y))


def start_func(func):
    def wrapper(*args, **kwargs):
        print(f'запуск функции')
        result = func(*args, **kwargs)
        return result
    return wrapper

@start_func
def greet():
    print("Hello world!")

greet()