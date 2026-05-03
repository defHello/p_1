def is_positive(x):
    return x > 0

numbers = [3, 0, -1]
print(list(filter(is_positive, numbers)))


numbers = [1, 0, -1]
print(list(filter(lambda x: x > 0, numbers)))