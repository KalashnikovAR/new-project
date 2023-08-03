N = int(input('Введите число: '))
num_list = []

for num in range(N + 1):
    if num % 2 != 0:
        num_list.append(num)
print('Список из нечетных чисел от одного до N: ', num_list)
