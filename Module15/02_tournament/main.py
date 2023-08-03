name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
day_list = []
for index, name in enumerate(name_list):
    if index % 2 == 0:
        day_list.append(name)
print(day_list)