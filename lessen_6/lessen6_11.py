import numpy as np

def add_row_to_all(n, m, l):
    matrix = np.random.randint(1, 10, (n, m))
    
    target_row = matrix[l-1]
    
    #Прибавляем её ко всей матрице
    result = matrix + target_row
    
    print("Исходная матрица:\n", matrix)
    print(f"\nСтрока №{l}, которую прибавляем: ", target_row)
    print("\nРезультат сложения:\n", result)

add_row_to_all(4, 3, 1)
