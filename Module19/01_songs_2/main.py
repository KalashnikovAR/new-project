violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

num = int(input('количество песен: '))
summ = 0
for i in range(num):
    song = input('Введите название {} песни: '.format(i+1))
    if violator_songs.get(song):
        summ += violator_songs.get(song)
    else:
        print('Такой песни нет в плэй-листе')
print('Общее время звучания песен: {} '.format(summ))