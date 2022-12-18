d = 160
b = 0
while True:
    a = int(input('Оплатить: '))
    if d - a < 0:
        print('Недостаточно средств!')
        break
    d -= a
    b += 1
print(f'Покупок сделано: {b}, остаток на карте: {d}')