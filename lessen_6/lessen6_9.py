# Реализовать функцию, которая находит сумму элементов
# матрицы (матрица M x N). Определить, какую долю в общей сумме
# (процент) составляет сумма элементов каждого столбца.

import numpy as np

def analyze_matrix_numpy(n, m):
    #Создаем матрицу случайных чисел
    matrix = np.random.randint(1, 11, size=(n, m))
    
    #Находим общую сумму
    total_sum = np.sum(matrix)
    
    #Находим суммы каждого столбца
    column_sums = np.sum(matrix, axis=0)
    
    #проценты
    percentages = (column_sums / total_sum) * 100
    
    print("Матрица:")
    print(matrix)
    print(f"\nОбщая сумма всех элементов: {total_sum}")
    print("-" * 35)
    
    for i, (col_sum, pct) in enumerate(zip(column_sums, percentages), 1):
        print(f"Столбец {i}: сумма = {col_sum:>3}, процент = {pct:>6.2f}%")

# Запуск
analyze_matrix_numpy(5, 3)
