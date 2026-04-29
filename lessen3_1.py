import math as m
import tkinter as tk
from tkinter import ttk

#создаем окно
root = tk.Tk()
root.title("Математика=)")
root.geometry('820x250')
root.resizable(False, False)

def matematika():
    a = float(numbers_1.get())
    b = float(numbers_2.get())
    x = float(numbers_3.get())
    #первая формула а)
    y = (m.pow(a, 2) / 3) + (m.pow(a, 2 + 4) / b) + (m.sqrt((m.pow(a, 2) + 4)) / 4) + m.sqrt(m.pow(m.pow(a, 2) + 4, 3)) / 4
    
    #вторая формула b)
    i = m.cos(x) + m.sin(x)
    
    #третья формула с)
    c = (m.cos(m.pow(x, 2))**2) + (m.sin(2 * x - 1)**2) ** 1/3

    #четвертая формула d)
    d = 5 * x + (3 * x) ** 2 * (m.sqrt(1 + (m.sin(x)**2)))
    
    #Расчет формулы а)
    numbers_4.delete(0, tk.END)  # очищаем поле
    numbers_4.insert(0, str(y))  # вставляем результат

    #Расчет формулы b)
    numbers_5.delete(0, tk.END)  # очищаем поле
    numbers_5.insert(0, str(i))  # вставляем результат

    #Расчет формулы с)
    numbers_6.delete(0, tk.END)  # очищаем поле
    numbers_6.insert(0, str(c))  # вставляем результат

     #Расчет формулы d)
    numbers_7.delete(0, tk.END)  # очищаем поле
    numbers_7.insert(0, str(d))  # вставляем результат

#Создаем поле ввода
numbers_1 = ttk.Entry()
numbers_1.grid(row=0, column=0, ipadx=0, ipady=1, sticky='nw', padx=5, pady=5)
label_1 = ttk.Label(text="Введите значение: а")
label_1.grid(row=1, column=0, ipadx=0, ipady=1, sticky='nw', padx=5, pady=5)

numbers_2 = ttk.Entry()
numbers_2.grid(row=0, column=1, ipadx=0, ipady=1, sticky='nw', padx=5, pady=5)
label_2 = ttk.Label(text="Введите значение: b")
label_2.grid(row=1, column=1, ipadx=0, ipady=1, sticky='nw', padx=5, pady=5)


numbers_3 = ttk.Entry()
numbers_3.grid(row=0, column=2, ipadx=0, ipady=1, sticky='nw', padx=5, pady=5)
label_3 = ttk.Label(text="Введите значение: x")
label_3.grid(row=1, column=2, ipadx=0, ipady=1, sticky='nw', padx=5, pady=5)

#Кнопка рассчета
result = ttk.Button(text='Расcчитать', command=matematika)
result.grid(row=2, column=0, columnspan=4, ipadx=10, ipady=6, pady=5)

#создаем поле вывода
numbers_4 = ttk.Entry()
numbers_4.grid(row=3, column=0, ipadx=0, ipady=1, sticky='nw', padx=5, pady=5)
label = ttk.Label(text="Формула: а")
label.grid(row=4, column=0, ipadx=0, ipady=1, sticky='nw', padx=5, pady=5)

numbers_5 = ttk.Entry()
numbers_5.grid(row=3, column=1, ipadx=0, ipady=1, sticky='n', padx=5, pady=5)
label = ttk.Label(text="Формула: b")
label.grid(row=4, column=1, ipadx=0, ipady=1, sticky='n', padx=5, pady=5)

numbers_6 = ttk.Entry()
numbers_6.grid(row=3, column=2, ipadx=0, ipady=1, sticky='ne', padx=5, pady=5)
label = ttk.Label(text="Формула: c")
label.grid(row=4, column=2, ipadx=0, ipady=1, sticky='ne', padx=5, pady=5)

numbers_7 = ttk.Entry()
numbers_7.grid(row=3, column=3, ipadx=0, ipady=1, sticky='ne', padx=5, pady=5)
label = ttk.Label(text="Формула: d")
label.grid(row=4, column=3, ipadx=0, ipady=1, sticky='ne', padx=5, pady=5)

root.mainloop()