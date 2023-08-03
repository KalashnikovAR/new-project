num = int(input('Количество видеокарт: '))
old_videocard_list = []
new_videocard_list = []

for old in range(num):
  card = input(f'Видеокарта {old+1}: ')
  old_videocard_list.append(card)

print('Старый список видеокарт:', '[', *old_videocard_list, ']')

for videocard in old_videocard_list:
    if videocard != max(old_videocard_list):
        new_videocard_list.append(videocard)
print('\nНовый список видеокарт: ', '[', *new_videocard_list, ']')