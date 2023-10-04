words_dict = dict()

count = int(input('Введите количество пар слов: '))

for i in range(1, count+1):
    word = input(f'{i} пара: ').lower().split(' - ')
    words_dict[word[0]] = word[1]
    words_dict[word[1]] = word[0]

while True:
    user_word = input('Введите слово: ').lower()
    if user_word in words_dict:
        print(f'Синоним: {words_dict[user_word]}')
    else:
        print('Такого слова в словаре нет.')
