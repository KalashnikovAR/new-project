first_str = list(input('Первая строка: '))
second_str = list(input('Вторая строка: '))
shift = 0

for i in range(len(first_str)+1):
    shift += 1
    second_str.insert(0, second_str.pop())
    if shift > len(first_str):
        print('Строку нельзя получить из второй с помощью циклического сдвига.')
        break
    elif second_str == first_str:
        print(f'Первая строка получается из второй со сдвигом {shift}.')
        break




