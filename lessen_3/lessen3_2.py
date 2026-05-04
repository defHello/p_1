import math as m
import tkinter as tk

first = tk.Tk()
first.title("Калькулятор кредита")
first.geometry("400x400")


def calcul():
    try:
        i = float(entry_i.get())
        s = float(entry_s.get())
        n = int(entry_n.get())

        p = i / 1200

        # Если ставка равна 0
        if p == 0:
            m = s / n
        else:
            numer = s * p * (1 + p) ** n
            denumer = (1 + p) ** n - 1
            m = numer / denumer

        total_pay = m * n  # сколько заплатит пользователь
        Uppay = total_pay - s  # переплата

        label_monthly.config(text=f"Ежемесячный платеж: {m:.2f}")
        label_total.config(text=f"Общая выплата: {total_pay:.2f}")
        label_overpay.config(text=f"Переплата: {Uppay:.2f}")

    except ValueError:
        label_monthly.config(text="Некорректный ввод")
        label_total.config(text="")
        label_overpay.config(text="")


tk.Label(first, text="Годовая ставка (в %):").pack(pady=5)
entry_i = tk.Entry(first)
entry_i.pack(pady=5)

tk.Label(first, text="Сумма займа:").pack(pady=5)
entry_s = tk.Entry(first)
entry_s.pack(pady=5)

tk.Label(first, text="Количество месяцев:").pack(pady=5)
entry_n = tk.Entry(first)
entry_n.pack(pady=5)

btn = tk.Button(first, text="Посчитать", command=calcul)
btn.pack(pady=10)

label_monthly = tk.Label(first, text="")
label_monthly.pack(pady=5)

label_total = tk.Label(first, text="")
label_total.pack(pady=5)

label_overpay = tk.Label(first, text="")
label_overpay.pack(pady=5)

first.mainloop()
