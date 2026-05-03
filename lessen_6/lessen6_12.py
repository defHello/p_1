# Программа получает на вход число H. Реализовать
# функцию, которая определяет, какие столбцы имеют хотя бы одно
# такое же число, а какие не имеют (матрица M x N).

import numpy as np

def find_h_in_columns(n, m, h) -> any:
    #Создаем матрицу
    matrix = np.random.randint(1, 11, (n, m))
    print("Матрица:")
    print(matrix)
    print(f"\nИщем число: {h}")
    print("-" * 20)

    #Проверяем наличие числа H в каждом столбц
    search_h = np.any(matrix == h, axis=0)

    #результат
    for i, found in enumerate(search_h, 1):
        status = f"содержит H" if found else "не содержит"
        print(f"Столбец {i}: {status}")

#ищем число 6
find_h_in_columns(4, 5, 6)
