# Реализовать функцию, которая перемножает элементы
# каждого столбца матрицы с соответствующими элементами K-го
# столбца (матрица M x N)

import numpy as np

def multiply_easy(n, m, k):
    matrix = np.random.randint(1, 10, (n, m))
    
    # Берем K-й столбец (индекс k-1)
    target_col = matrix[:, [k-1]]
    result = matrix * target_col
    
    print("Матрица:\n", matrix)
    print(f"\n{result}")

multiply_easy(3, 4, 2)
