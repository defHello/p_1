name = input('Как вас зовут?  ') #запрашиваем имя пользователя
print(f'Hello, my friends - {name}!\nВы приехали на заправку - Python.') #приветствуем пользователя
print('Помогу вам рассчитать стоймость поездки и количество бензина')
#требуем данные пользователя
distance = float(input('Введите расстояние: '))
litr = float(input('Введите расход топлива на 100 км '))
price = float(2.64)
litr = (distance * litr) / 100
total = litr * price
#Вывод результата
print(f'Для поездки на расстояние {distance}, вам потребуется: {litr} литров.\nБудет затрачено денег:', total, 'р.')
print('Good Bye!')


def azs(distance, litr, price):
    ltr = distance * litr / 100
    total = ltr * price
    return ltr, total
distance = float(input('Введите расстояние: '))
litr = float(input('Введите расход топлива на 100 км '))
price = float(2.64)
print(azs(distance=distance,
           litr=litr,
           price=price
      )
)