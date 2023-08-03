num = int(input('Введите длину списка: '))
num_list = [(x - x + 1 if x % 2 == 0 else x % 5) for x in range(num)]

print(num_list)
