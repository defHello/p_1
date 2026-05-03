target = 8
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search_recursive(numbers, target, left, right):
    if left > right:
        return -1
    
    m = (left + right) // 2
    if numbers[m] == target:
        return m
    
    elif numbers[m] > target:
        return binary_search_recursive(numbers, target, left, m - 1)
    else:
        return binary_search_recursive(numbers, target, m + 1, right)

result = binary_search_recursive(numbers, target, 0, len(numbers) - 1)
print(result)
