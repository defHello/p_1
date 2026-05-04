from typing import Callable


# --- 1. Определяем конкретные именованные функции ---


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
        print("Ошибка: Деление на ноль!")
        return 0
    return x / y


def power(x: float | int, y: float | int) -> float | int:
    """Возводит x в степень y."""
    return x**y


# --- 2. Функция высшего порядка ---


def execute_operation(
    a: float | int,
    b: float | int,
    func: Callable[[float | int, float | int], float | int],
) -> float | int:
    """
    Принимает два числа и функцию, реализующую операцию.
    Это 'чистая' функция высшего порядка.
    """
    return func(a, b)


# --- 3. Организация интерфейса через словарь ---

# Ключи — это строки (названия команд), значения — сами объекты функций
operations: dict[str, Callable[[float | int, float | int], float | int]] = {
    "+": lambda x, y: x + y,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
}

# --- 4. Пример работы программы ---


def main():
    x, y = 10, 2

    print(f"Исходные числа: {x} и {y}\n" + "-" * 20)

    for symbol, func in operations.items():
        result = execute_operation(x, y, func)
        print(f"Операция [{symbol}]: {result}")


if __name__ == "__main__":
    main()


# Попробуй добавить в этот код функцию modulo(x, y), которая возвращает остаток от деления, и интегрируй её в словарь
# Переписать на лямбды
