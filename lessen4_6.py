target = 7
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

left, right = 0, len(n) - 1
while left <= right:
    m = left + ((right - left) // 2)
    if n[m] == target:
        print(m)
        break
    elif n[m] > target:
        right = m - 1
    elif n[m] < target:
        left = m + 1