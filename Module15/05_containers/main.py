containers = int(input('Количество контейнеров: '))
containers_list = []
for _ in range(containers):
    weight = int(input('Введите вес контейнера: '))
    containers_list.append(weight)

containers_list.sort(reverse=True)

index = len(containers_list)

new_container = int(input('Введите вес нового контейнера: '))

for i in range(len(containers_list)):
    if containers_list[i] <= new_container:
        index = i
        break
print('Номер, который получит новый контейнер: ', index + 1)
