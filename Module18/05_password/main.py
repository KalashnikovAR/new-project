while True: 
    password = input('Придумайте пароль: ')
    length = len(password)
    capital = len([letter for letter in password if letter.isupper()])
    num = len([number for number in password if number.isdigit()])
    if length >= 8 and capital >= 1 and num >= 3:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
