#1
try:
    def sum_numbers(a, b):
        if operation == '+':
            return a + b
        elif operation == '-':
            return a - b
        elif operation == '*':
            return a * b
        elif operation == '/':
            return a / b

    num_1 = float(input("Введите значение: "))
    num_2 = float(input("Введите значение: "))
    operation = input("Выберите операцию: +, -, *, /: ")
    print(sum_numbers(num_1, num_2))

except ZeroDivisionError:
    print("Делить на ноль нельзя")
except ValueError:
    print("Некорректное значение")

#отнимание + сложение 
def three_numbers(a, b, c):
    return (a - b) + c

num_1 = float(input("Введите значение: "))
num_2 = float(input("Введите значение: "))
num_3 = float(input("Введите значение: "))

print(three_numbers(num_1, num_2, num_3))

#произведение + деление
def three_numbers(a, b, c):
    return (a * b) / c

num_1 = float(input("Введите значение: "))
num_2 = float(input("Введите значение: "))
num_3 = float(input("Введите значение: "))

print(three_numbers(num_1, num_2, num_3))

#остаток от деления

def three_numbers(a, b, c):
    return (a + b) % c

num_1 = float(input("Введите значение: "))
num_2 = float(input("Введите значение: "))
num_3 = float(input("Введите значение: "))

print(three_numbers(num_1, num_2, num_3))


#2
def square (cat_a, cat_b):
    return (cat_a * cat_b) / 2
try:
    a = int(input())
    b = int(input())
except ValueError:
    print("Введите корректное значение")
print(square(a, b))

def hypotenuse (cat_a, cat_b):
    return (cat_a**2 + cat_b**2)**(1/2)
try:   
    a = int(input())
    b = int(input())
except ValueError:
    print("Введите корректное значение")
print(hypotenuse(a, b))


#3
text = 'Hellow World' 'test' 'test1' 'test2 test3 test4'
text_new = text.split()
print(text_new)

#4
text = "hhhabchghhh"
print(text[0] + text[1 : -1].replace("h", "H") + text[-1])

#5
text_1 = "Hello"
print(text_1[2])
text_2 = "Hello"
print(text_2[-2])
text_3 = "Hello"
print(text_3[0:5])
text_4 = "Hello"
print(text_4[0:4])
text_5 = "Hello"
print(text_4[0:6:2])
text_6 = "Hello"
print(text_6[1:4:2])
text_7 = "Hello"
print(text_7[::-1])
text_8 = "Hello"
print(text_8[-1:-8: -2])
text_9 = "Hello"
print(len(text_9))

#6
numbers = 200
end_numbers = numbers % 10
print(end_numbers)

numbers = 123
end_numbers = numbers % 10
print(end_numbers)

numbers = 587
end_numbers = numbers % 10
print(end_numbers)

#7
numbers = 123
numbers_1 = (numbers // 10) % 10
print(numbers_1)

numbers = 978
numbers_2 = (numbers // 10) % 10
print(numbers_2)

#8
numbers = 123
summa = (numbers // 100) + ((numbers // 10) % 10) + (numbers % 10)
print(summa)

numbers = 555
summa = (numbers // 100) + ((numbers // 10) % 10) + (numbers % 10)
print(summa)