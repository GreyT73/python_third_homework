#Задача 16: Требуется вычислить, сколько раз встречается некоторое
#число X в массиве A[1..N]. Пользователь в первой строке вводит
#натуральное число N – количество элементов в массиве. В последующих
#строках записаны N целых чисел Ai
#. Последняя строка содержит число X

x = int(input("Enter a number: "))
n = int(input("Enter a list length: "))
count_x = 0
A = [i for i in range(1, n + 1)]
print(x)
for index in range(len(A)):
    if A[index] == x:
        count_x += 1
print(f"Число {x} в списке {A} встречается  {count_x} раз")
