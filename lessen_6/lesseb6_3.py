# Программа получает на вход число. Реализовать
# функцию, которая определяет, является ли это число простым
# (делится только на единицу и на само себя).

def prime_number(n: int) -> int:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Введите число: "))
if prime_number(n):
    print("Число простое")
else:
    print("Число составное")
