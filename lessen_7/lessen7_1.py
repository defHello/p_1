def convert_to_str(x):
    return list(str(x))

numbers = [1, 2, 3]
print(list(map(convert_to_str, numbers)))

numbers = [1, 2, 3]
print(list(map(str, numbers)))