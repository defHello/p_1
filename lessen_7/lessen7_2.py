def maximum(x):
    if x > 0:
        return True
    else:
        return False
numbers = [1, 0, -1]
print(list(filter(maximum, numbers)))


numbers = [1, 0, -1]
print(list(filter(lambda x: x > 0, numbers)))