def divider(num):
    min_divider = num
    for i in range(num-1, 1, -1):
        if (num % i == 0):
            if (min_divider > i):
                min_divider = i
    return(min_divider)

num = int(input("Введите число: "))
print('Наименьший делитель, отличный от единицы: ', divider(num))
