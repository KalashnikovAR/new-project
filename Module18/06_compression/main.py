string = input('введите строку: ')
count = 0         #счетчик повторений
shifr = ''     #итоговый результат
for i in range(len(string)):
    count += 1
    if i == len(string) - 1:
        shifr = shifr + string[i] + str(count)
        break
    if string[i] != string[i+1]:
        shifr = shifr + string[i] + str(count)
        count = 0
print(shifr)
