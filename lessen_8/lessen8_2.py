# Реализовать программу с функционалом калькулятора
# для операций над двумя числами. Числа и операция вводятся
# пользователем с клавиатуры. Использовать обработку
# исключений

from typing import Callable

def add(x: float | int, y: float | int) -> float | int:
    """Возвращает сумму двух чисел."""
    return x + y


def subtract(x: float | int, y: float | int) -> float | int:
    """Возвращает разность."""
    return x - y


def multiply(x: float | int, y: float | int) -> float | int:
    """Возвращает произведение."""
    return x * y


def divide(x: float | int, y: float | int) -> float | int:
    """Возвращает частное. Обрабатывает деление на ноль."""
    if y == 0:
        raise ZeroDivisionError("Ошибка: Делить на ноль нельзя!")
    return x / y


def power(x: float | int, y: float | int) -> float | int:
    """Возводит x в степень y."""
    return x**y

operations: dict[str, Callable[[float | int, float | int], float | int]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
}

def get_user():
    """Работаем с пользователем. Запрашиваем пользовательские данные"""
    
    print("Доступные операции:", ", ".join(operations.keys()))
    print("Введите 'выход' для завершения.")

    while True:
        try:

            #Выбирает операцию
            choice = input("\nВыберите операцию: ").strip()

            #Для выхода из цикла
            if choice.lower() == 'выход':
                break

            #Продолжаем, если пользователь не правильно выбрал операцию
            if choice not in operations:
                print("Ошибка: Неизвестная операция!")
                continue

            num_1 = float(input("Введите первое число: "))
            num_2 = float(input("Введите второе число: "))

            func = operations[choice]
            result = func(num_1, num_2)
            
            print(f"Результат: {result}")

        except ValueError:
            print("Ошибка: Введите корректные числа!")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    get_user()