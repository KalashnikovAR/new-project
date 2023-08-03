def cipher(string, user_shift):
    cipher_list = [(alphabet[(alphabet.index(sym) + user_shift) % 33] if sym != ' ' else ' ') for sym in string]
    new_string = ''
    for i in cipher_list:
        new_string += i
    return new_string


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
txt = input('Введите текст: ')
shift = int(input('Введите сдвиг: '))

output = cipher(txt, shift)
print(output)
