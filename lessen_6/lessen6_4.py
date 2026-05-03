# Программа получает на вход два числа и находит их НОД
# (наибольший общий делитель). Пример: на вход подаются числа 12
# и 18, их НОД равен 6

from math import gcd

def gcd(m, n):
    while m!=n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n

a = int(input("Введите первое число: "))
b = int(input("Введите второе число"))

print(gcd(a, b))