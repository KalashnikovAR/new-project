def summ(number):
    count = 0
    while number > 0:
        x = number % 10
        count += x
        number = number // 10
    return(count)

def digit_count(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return(count)


number = int(input('Введите число: '))

print('Сумма чисел: ', summ(number), '\nколичество цифр в числе: ', digit_count(number), '\nРазность суммы и количества цифр: ', summ(number)-digit_count(number))