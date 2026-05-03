# Дана матрица M x N. Исходная матрица состоит из нулей и
# единиц. Реализовать функцию, которая добавит к матрице ещё
# один столбец, элементы которого делает количество единиц в
# соответствующей строке чётным

from random import randint

n, m = 4, 4
# Создаем матрицу
matrix = [[randint(0, 1) for _ in range(m)] for _ in range(n)]

print("Матрица до:")
for r in matrix: print(r)

for row in matrix:
    ones_count = row.count(1)
    row.append(1 if ones_count % 2 != 0 else 0)

print("\nМатрица после:")
for r in matrix: print(r)

