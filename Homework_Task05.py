# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
k = 8


def fibonacci(k: int) -> list:
    if k == 1:
        return [1]
    elif k == 2:
        return [1, 1]
    fib_list = fibonacci(k - 1)
    fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


def nego_fibonacci(fib_list: list):
    nego_fib_list = fib_list.copy()
    nego_fib_list.insert(0, 0)
    for i, fib in enumerate(fib_list):
        if i % 2 != 0:
            nego_fib_list.insert(0, fib * (-1))
        else:
            nego_fib_list.insert(0, fib)
    return nego_fib_list


print(nego_fibonacci(fibonacci(k)))
