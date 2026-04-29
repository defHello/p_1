def fibonacci_list(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

numbers = int(input('Введите значение: '))
print(fibonacci_list(numbers))