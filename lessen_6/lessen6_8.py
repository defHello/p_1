# Реализовать функцию, которая находит минимальный и
# максимальный элементы в матрице (матрица M x N). Вывести в
# консоль индексы найденных элементов.

from random import randint

#Функция создания матрицы
def create_matrix(n, m):
    return [[randint(1, 100) for _ in range(m)] for _ in range(n)]

# Параметры
n, m = 5, 3
matrix = create_matrix(n, m)

#Вывод матрицы для проверки
print()
for row in matrix:
    print(*row)

# Поиск минимума и максимума
min_val = matrix[0][0]
max_val = matrix[0][0]
min_index = (0, 0)
max_index = (0, 0)

for i in range(n):        # Цикл по строкам
    for j in range(m):    # Цикл по столбцам
        current = matrix[i][j]

        # Проверка на минимум
        if current < min_val:
            min_val = current
            min_index = (i, j)
            
        # Проверка на максимум
        if current > max_val:
            max_val = current
            max_index = (i, j)

print(f"Минимум: {min_val} (индекс: {min_index})")
print(f"Максимум: {max_val} (индекс: {max_index})")


    
