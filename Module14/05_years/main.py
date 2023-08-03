def years(first, second):
    print('Годы от ', first, 'до', second, 'с тремя одинаковыми цифрами: ')
    for year in range(first, second + 1):
        first_num = year // 1000
        second_num = (year // 100) % 10
        third_num = (year // 10) % 10
        fourth_num = year % 10
        if (first_num == second_num == third_num) or (second_num == third_num == fourth_num) or (third_num == fourth_num == first_num):
            print(year)


first = int(input('Введите первый год: '))
second = int(input('Введите второй год: '))
years(first, second)
