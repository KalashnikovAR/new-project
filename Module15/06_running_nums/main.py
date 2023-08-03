x = [1, 2, 3, 4, 5]

shift = int(input('Сдвиг: '))
print('Исходный список: ', x)
for i in range(shift):
    x.insert(0, x.pop())

print('Сдвинуый список: ', x)


