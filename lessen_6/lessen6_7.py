# Реализовать функцию, которая создаёт матрицу размером
# M строк на N столбцов и заполняет её рандомными числами
from random import randint

def matrixa(n, m):
    matrix = [[randint(1,10)for _ in range(m)]for _ in range(n)]
    return matrix
    
n, m = 5, 3

for row in matrixa(m, n):
    print(*row)