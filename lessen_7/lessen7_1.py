def stringer(x):
    return list(str(x))

numbers = [1, 2, 3]
print(list(map(stringer, numbers)))

numbers = [1, 2, 3]
print(list(map(str, numbers)))