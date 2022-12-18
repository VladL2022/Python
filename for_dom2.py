n = input('Введите десятизначное число: ')
a = str()
for i in str(n):
    if int(i) % 2 == 0:
        a += i
print(a)