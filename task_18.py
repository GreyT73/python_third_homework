#Задача 18: Требуется найти в массиве A[1..N] самый близкий по
#величине элемент к заданному числу X. Пользователь в первой строке
#вводит натуральное число N – количество элементов в массиве. В
#последующих строках записаны N целых чисел Ai
#. Последняя строка
#содержит число X


a = []
x = int(input("Введите число: "))
n = int(input("Введите длину массива: "))

for i in range(n):
    a.append(int(input(f"Введите число под номером {i + 1}: ")))

min_dif = abs(x - a[0])
dif = a[0]
number = a[0]
for index in range(1, len(a)):
    dif = abs(x - a[index])
    if dif < min_dif:
        min_dif = dif
        number = a[index]
print(f"Ближайшим числом по модулю к {x} в массиве {a} является является {number}")