target = 2
n = [5, 6, 7, 1, 2, 3, 4]
left, right = 0, len(n) - 1
print(left, right)
while left <= right:
    m = left + ((right - left) // 2)
    if n[m] == target:
        print(f'{m}')
        break
    if n[left] <= n[m]:
        if n[left] <= target and target < n[m]:
            right = m - 1
        else:
            left = m + 1
    else:
        if n[m] < target <= n[right]:
            left = m + 1
        else:
            right = m - 1


