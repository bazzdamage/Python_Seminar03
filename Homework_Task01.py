# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
numbers = [2, 3, 5, 9, 3]
sum = 0
for i, num in enumerate(numbers):
    if i % 2 != 0:
        sum += num
print(sum)