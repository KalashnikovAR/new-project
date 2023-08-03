def check_coin_location():
    print('Введите координату монетки: ')
    x = float(input("X: "))
    y = float(input("Y: "))
    r = float(input("Введите радиус: "))

    distance_from_center = (x**2 + y**2)**0.5
    if distance_from_center <= r:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")

check_coin_location()
