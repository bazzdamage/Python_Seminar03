# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
numbers = [1.1, 1.2, 3.1, 5, 10.01]
frac_numbers = []
for num in numbers:
    frac = round(num % 1, 2)
    if frac > 0:
        frac_numbers.append(frac)
print(frac_numbers)
print(max(frac_numbers) - min(frac_numbers))
