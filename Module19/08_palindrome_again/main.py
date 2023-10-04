def is_poly(string):
    sym = {}
    for i_sym in string:
        sym[i_sym] = sym.get(i_sym, 0) + 1

    count = 0
    for value in sym.values():
        if value % 2 != 0:
            count += 1

    return count <= 1


text = input('Введите строку: ')

if is_poly(text):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')