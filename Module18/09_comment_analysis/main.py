text = input("Введите строку для анализа: ")
lowercase = 0
uppercase = 0
for i in text:
    if i.islower():
        lowercase += 1
    else:
        uppercase += 1
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
