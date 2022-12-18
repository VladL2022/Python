a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a > b:
    a, b = b, a
for i in range(a, b):
    if i < 0:
        print(i)