numbers = [1, 17, 16, 4, 5, 9, 9, 5, 2, 9, 10, 13]
quantity =  len(numbers) == len(set(numbers)) #проверяем на одинаковое колтчество чтобы исключить повторы
print(f'{quantity}')
numbers_dict = {}
for i in numbers:
    numbers_dict[i] = numbers_dict.get(i, 0) + 1
print(numbers_dict.values())

for key, value in numbers_dict.items():
    if value >= 2:
        print(f'Число {key} встречается: {value}')