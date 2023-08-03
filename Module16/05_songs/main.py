def duration(time):
    for elem in time:

        if isinstance(elem, float):
            return elem


violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
minutes = 0
songs = int(input('Сколько песен выбрать? '))
for i in range(songs):
    user_song = input(f'Название {i+1}-й песни: ')
    for choice in violator_songs:
        if user_song in choice:
            minutes += duration(choice)
print(f'Общее время звучания песен —  {minutes}')
