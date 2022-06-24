'''
Практическая №13
Вариант №32
1.В последовательности на n целых чисел умножить все элементы на первый
максимальный элемент.
'''
numbers = input('Введите последовательность чисел : ')
arr = list(map(int, numbers.split()))
print(arr)

max_number = max(arr)
print('максимальное число: ', max_number)

new_arr = []
for num in arr:
    new_arr.append(num * max_number)
print('новая последовательность: ', new_arr)


