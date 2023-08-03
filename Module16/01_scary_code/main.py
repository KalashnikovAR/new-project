a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
print('Количество цифр 5 при первом объединении: ', a.count(5))
for i_elem in a:
    if i_elem == 5:
        a.remove(i_elem)
a.extend(c)
print('Количество цифр 3 при втором объединении: ', a.count(3))

print(a)