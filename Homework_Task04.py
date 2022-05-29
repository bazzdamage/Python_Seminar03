# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number = 45
binary_num = ''
while number > 0:
    binary_num = f"{number % 2}" + binary_num
    number //= 2
print(binary_num)
