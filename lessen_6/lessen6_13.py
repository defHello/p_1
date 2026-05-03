# Реализовать функцию, которая находит сумму элементов
# на главной диагонали и сумму элементов на побочной диагонали
# (матрица M x N)

import numpy as np

def diagonal_sums(n, m) ->any:
    # Создаем квадратную матрицу
    matrix = np.random.randint(1, 10, (n, m))
    print("Матрица:\n", matrix)

    #Сумма главной диагонали (слева направо)
    main_diag_sum = np.trace(matrix) 
    
    #Сумма побочной диагонали (справа налево)
    side_diag_sum = np.trace(np.fliplr(matrix))

    print(f"\nСумма главной диагонали: {main_diag_sum}")
    print(f"Сумма побочной диагонали: {side_diag_sum}")
diagonal_sums(4, 4)
