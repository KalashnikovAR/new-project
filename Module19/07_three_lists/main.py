def intersection(num_1, num_2, num_3):
    inter = []
    for i_num in num_2:
        if i_num in num_1 and i_num in num_3:
            inter.append(i_num)

    return inter


def difference(num_1, num_2, num_3):
    inter = []
    for i_num in num_1:
        if i_num not in num_2 and i_num not in num_3:
            inter.append(i_num)

    return inter


array_1 = {1, 5, 10, 20, 40, 80, 100}
array_2 = {6, 7, 20, 80, 100}
array_3 = {3, 4, 15, 20, 30, 70, 80, 120}

print('задача 1: ')

print('Решение с множествами: ', end='')
print(*array_1 & array_2 & array_3, sep=', ')

print('Решение без множеств: ', end='')
print(*intersection(array_1, array_2, array_3), sep=', ')


print('Задача 2: ')

print('Решение с множествами: ', end='')
print(*(array_1 - (array_2 | array_3)), sep=', ')

print('Решение без множеств: ', end='')
print(*difference(array_1, array_2, array_3), sep=', ')
