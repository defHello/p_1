def body_mass_index(weight: float, height: float) -> str:
    """ Производим вычесления <Индекса Массы Тела>"""
    if height > 3:
        height /= 100
    bmi = weight / height ** 2

    if bmi < 18.5:
        result = 'Дефицит массы тела'
    elif bmi < 25:
        result = 'Нормальная масса тела'
    elif bmi < 30:
        result = 'Избыточная масса тела'
    else:
        result = 'Ожирение'
    
    return f"Ваш индекс массы тела составляет: {round(bmi, 1)}\nВы находитесь: {result}"

def get_user():
    """Работаем с пользователем. Запрашиваем пользовательские данные"""
    try:
        weight_input = float(input("Введите ваш вес (кг): "))
        if weight_input <= 0:
            raise ValueError("Вес должен быть положительным")
        height_input = float(input("Введите ваш рост(см или метры): "))
        if height_input <= 0:
            raise ValueError("Рост должен быть положительным")
        print(body_mass_index(weight_input, height_input))
    except ValueError as e:
        print(f'Ошибка: {e}')
    except ZeroDivisionError as e:
        print(f'Рост не может быть равен: 0, {e}')

if __name__ == "__main__":
    get_user()