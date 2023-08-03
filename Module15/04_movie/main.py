films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
wish_list = []

like = int(input('Сколько фильмов хотите добавить?: '))
for _ in range(like):
    film = input('Введите название фильма: ')
    if film.capitalize() in films:
        wish_list.append(film)
    else:
        print('Ошибка: фильма ', film, 'у нас нет :(')
print('Ваш список любимых фильмов: ', wish_list)
