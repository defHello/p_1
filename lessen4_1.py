import math as m
#sin(x)
def sinus(x, n):
    a = 0
    for i in range(n):
        power = 2 * i + 1 #фактриал и степень (они равны)
        sign = (-1) ** i #чередуем + и -
        sin_a = sign * (x**power / m.factorial(power))
        a += sin_a
    return a
print(sinus(2, 5))

#cos(x)
def cosinus(x, n):
    a = 0
    for i in range(n):
        power = i * 2 #фактриал и степень (они равны)
        sign = (-1) ** i #чередуем + и -
        cos_a = sign * (x**power / m.factorial(power))
        a += cos_a
    return a
print(cosinus(2, 5))


