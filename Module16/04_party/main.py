def amount(num):
    name = input('Имя гостя: ')
    if num >= 6:
        print(f'Прости {name}, но мест нет')
    else:
        print(f'Привет {name}!')
        guests.append(name)


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек: ', *guests)
    guest = input('Гость пришел или ушел?: ').lower()
    if guest == 'пришел':
        amount(len(guests))
    elif guest == 'ушел':
        name = input('Имя гостя: ')
        print(f'Пока {name}')
        guests.remove(name)
    elif guest == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break


