letter = 'аоуыэеёиюя'
text = input("Введите текст: ")
vowels = [c for c in text if c in letter]
print("Список гласных букв:", vowels)
print("Длина списка:", len(vowels))
