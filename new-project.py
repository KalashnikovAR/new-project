# MyProfile app

SEPARATOR = '------------------------------------------'

# личная информация
name = '-'
age = 10
phone = '-'
phone_number = '-'
email = '-'
index = '-'
adress = '-'
dopinfo = ''
# Информация о предпринимателе
ogrnip = 0
inn = 0
checking_account = 0
bank = '-'
bik = 0
correspondent_account = 0


# для вывода личной информации
def personal_information(name, age, phone, email, index, adress, dopinfo):
    print(SEPARATOR)
    print('Имя:    ', name)
    if 11 <= age % 100 <= 19:
        years = 'лет'
    elif age % 10 == 1:
        years = 'год'
    elif 2 <= age % 10 <= 4:
        years = 'года'
    else:
        years = 'лет'

    print('Возраст:', age, years)
    print('Телефон:', phone)
    print('E-mail: ', email)
    print('Индекс: ', user_index)
    print('Почтовые адрес: ', adress)
    if dopinfo:
        print('')
        print('Дополнительная информация:')
        print(dopinfo)


def check_num(num, length, type):  # Проверка на длинну введенного числа
    correct = False
    while not correct:
        if len(str(num)) < length:
            print(f'\nОшибка ввода! Должно быть не менее {length} цифр\n')
        else:
            correct = True
            continue
        num = input('Попробуйте еще раз: ')


def check_is_num(num, type):  # проверка на ввод именно числа, а не строки
    while num == 0:
        try:
            num = int(input(f'Введите {type}: '))
            return num
        except ValueError:
            print('Неверный формат')


# ____________________________________________________________________________________

# Основная программа:

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # ГЛАВНОЕ МЕНЮ
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    choice = int(input('Введите номер пункта меню: '))
    if choice == 0:
        print('\nЗавершение работы ... ')
        break
    elif choice == 1:
        # ПОДМЕНЮ: ВВЕСТИ ИНФОРМАЦИЮ
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')
            choice_2 = int(input('Введите номер пункта меню: '))

            if choice_2 == 0:
                break
            if choice_2 == 1:
                name = input('Введите имя: ')
                while 1:
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    else:
                        print('Возраст не может быть отрицательным')
                phone = input('Введите номер телефона: ')
                phone_number = ''
                for i in phone:
                    if i == '+' or ('0' <= i <= '9'):
                        phone_number += i
                email = input('Введите адрес электронной почты: ')
                index = input('Введите почтовый индекс: ')
                user_index = ''
                for num in index:
                    if '0' <= num <= '9':
                        user_index += num
                adress = input('Введите почтовый адрес: ')

                dopinfo = input('Введите дополнительную информацию:\n')
            elif choice_2 == 2:
                ogrnip = 0
                inn = 0
                checking_account = 0
                bank = '-'
                bik = 0
                correspondent_account = 0

                type = 'ОГРНИП'
                ogrnip = check_is_num(ogrnip, type)
                check_num(ogrnip, 15, type)

                type = 'ИНН'
                inn = check_is_num(inn, type)

                type = 'Расчетный счет'
                checking_account = check_is_num(checking_account, type)
                check_num(checking_account, 20, type)

                bank = input('Введите наименование банка: ')

                type = 'БИК'
                bik = check_is_num(bik, type)

                type = 'Корреспондентский счет'
                correspondent_account = check_is_num(correspondent_account, type)
            else:
                print('Введите корректный пункт меню')

    elif choice == 2:
        # ПОДМЕНЮ 2: ВЫВЕСТИ ИНФОРМАЦИЮ
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                personal_information(name, age, phone_number, email, index, adress, dopinfo)

            elif option2 == 2:
                personal_information(name, age, phone_number, email, index, adress, dopinfo)

                # ВЫВОД ИНФОРМАЦИИ О ПРЕДПРИНИМАТЕЛЕ
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП: ', ogrnip)
                print('ИНН: ', inn)
                print('Расчетный счет: ', checking_account)
                print('Нименование банка: ', bank)
                print('БИК: ', bik)
                print('Корреспондентский счет: ', correspondent_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Ошибка ввода! Введите корректный пункт меню ')
