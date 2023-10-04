count = int(input('Введите количество заказов: '))
database = dict()
for i in range(1, count+1):
    order = input('{} заказ: '.format(i)).split()
    if order[0] in database:
        if order[1] in database[order[0]]:
            database[order[0]][order[1]] += int(order[2])
        else:
            database[order[0]][order[1]] = int(order[2])
    else:
        database[order[0]] = dict({order[1]: int(order[2])})

for elem1 in sorted(database):
    print(f'\n{elem1}: ')
    for elem2 in sorted(database[elem1]):
        print(f'\t{elem2}: {database[elem1][elem2]}')

