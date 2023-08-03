text = input('Введите строку: ')
biggest = max(text.split(), key=len)
print(f'Самое длинное слово: {biggest} \nДлинна этого слова: {len(biggest)}')
