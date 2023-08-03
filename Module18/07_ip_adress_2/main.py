while True:
    ip_adress = input('Введите IP: ')
    if ip_adress.count('.') != 3:
        print('Адрес — это четыре числа, разделённые точками.')
    else:
        list_numbers = ip_adress.split('.')
        for numbers in list_numbers:
            if not numbers.isdigit():
                print(f'{numbers} - это не целое число.')
                break
            elif int(numbers) > 255:
                print(f'{numbers} превышает 255.')
                break
        else:
            print('IP-адрес корректен.')
            break
