n = input('Введите трехзначное число: ')
leng = len(n)
if leng == 3 and int(n[0]) != 0:
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])
    print('Сумма цифр числа:', a + b + c)
else:
    print("Введите трехзначное число!")