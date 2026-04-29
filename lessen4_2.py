def masha(n, k):
    week_seven = k * (7-1)
    total_week = n // week_seven
    if n % week_seven != 0:
        extra_days = n % week_seven
        ostatok_days = extra_days // k
        if extra_days % k != 0:
            ostatok_days = ostatok_days + 1
    else:
        ostatok_days = 0
    days_work = (total_week * 6) + ostatok_days
    return days_work
tele = int(input())
money = int(input())
print(masha(tele, money))

