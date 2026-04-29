import tkinter as tk
import math as m

first = tk.Tk()
first.title("Расчет длины года на планетах")
first.geometry("400x400")


def calcul():
    try:
        a1 = float(entry_a1.get())
        b1 = float(entry_b1.get())
        a2 = float(entry_a2.get())
        b2 = float(entry_b2.get())

        # Формула для каждой планеты:
        # длина орбиты (в часах)
        a1_hours = (2 * m.pi * a1 * 1_000_000) / a2
        b2_hours = (2 * m.pi * b1 * 1_000_000) / b2

        # Переводим в дни
        a1_days = a1_hours / 24
        b2_days = b2_hours / 24

        label_a1.config(text=f"Длина года на первой планете: {a1_days:.2f} дней")
        label_b2.config(text=f"Длина года на второй планете: {b2_days:.2f} дней")

        if a1_days > b2_days:
            res = "Да, на первой планете год длиннее."
        else:
            res = "Нет, на первой планете год не длиннее."
        label_comparison.config(text=res)

    except ValueError:
        label_a1.config(text="Некорректные данные")
        label_b2.config(text="")
        label_comparison.config(text="")


# 1 планета
tk.Label(first, text="Первая планета").pack(pady=5)
tk.Label(first, text="Радиус R (млн км):").pack()
entry_a1 = tk.Entry(first)
entry_a1.pack(pady=5)

tk.Label(first, text="Орбитальная скорость v (км/ч):").pack()
entry_b1 = tk.Entry(first)
entry_b1.pack(pady=5)

# 2 планета
tk.Label(first, text="Вторая планета").pack(pady=5)
tk.Label(first, text="Радиус R (млн км):").pack()
entry_a2 = tk.Entry(first)
entry_a2.pack(pady=5)

tk.Label(first, text="Орбитальная скорость v (км/ч):").pack()
entry_b2 = tk.Entry(first)
entry_b2.pack(pady=5)


btn = tk.Button(first, text="Рассчитать", command=calcul)
btn.pack(pady=10)


label_a1 = tk.Label(first, text="")
label_a1.pack(pady=5)

label_b2 = tk.Label(first, text="")
label_b2.pack(pady=5)

label_comparison = tk.Label(first, text="")
label_comparison.pack(pady=10)


first.mainloop()
