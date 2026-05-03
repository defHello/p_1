# Программа получает на вход число в десятичной
# системе счисления. Реализовать функцию, которая
# переводит входное число в двоичную систему счисления.
# Допускается реализация функции как в рекурсивном
# варианте, так и с итеративным подходом.


def binary_ystem(n: int) ->int:
    if n == 0:
        return 0
    result = []
    while n > 0:
        remainder = n % 2
        result.append(remainder)
        n = n // 2
    return list(reversed(result))

n = int(input("Введите число для перевода: "))
print(binary_ystem(n))
