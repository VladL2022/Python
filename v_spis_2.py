a = [4, 6, 'pу', 'tell', 78]
b = [44, 'hello', 56, 'exept', ['world', 5.7], 3, 6]

c = a + b
print("Сложение двух списков:", c)

c.insert(2, 6)
print("Добавление элемента 6 на 3 позицию:", c)

count_six = c.count(6)
print("Количество вхождений числа 6:", count_six)

list_length = len(c)
print("Количество элементов списка:", list_length)

first_element_nested = c[10][0]
print("Первый элемент вложенного списка:", first_element_nested)
