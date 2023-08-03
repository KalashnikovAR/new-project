skates = int(input('Количество коньков: '))
skates_list = []
count = 0
for i in range(skates):
    size_skates = int(input(f'Размер пары {i+1}: '))
    skates_list.append(size_skates)

skates_list.sort()

people = int(input('Количество людей: '))
for i in range(people):
    people_size = int(input(f'Размер ноги {i+1} человека: '))
    for size in skates_list:
        if size >= people_size:
            count += 1
            skates_list.remove(size)
            break

print(f'Наибольшее количество людей, которые могут взять ролики: {count}')
