def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


text = 'здесь что-то написано'
hist = histogram(text)
print('Оригинальный словарь частот: ')
for i in sorted(hist.keys()):
    print(i, ':', hist[i])

text_dict = dict()

print('\nИнвертированный словарь частот: ')
for letter in set(text):
    text_dict[text.count(letter)] = text_dict.get(text.count(letter), []) + [letter]
for i in text_dict:
    print(i, ":", text_dict[i])

