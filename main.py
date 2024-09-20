import price
import check_input as check

print("Выберите деталь:\n1 - капот\n2 - передняя дверь\n3 - задняя дверь\n4 - передний бампер\n5 - задний бампер\n6 - крыша")
try:
    part = int(input("Номер выбранной детали: "))
except ValueError:
    print("Можно вводить только числа")
else:
    while not check.check_input(part, "detail"):
        print("Введите число от 1 до 6")
        part = int(input("Номер выбранной детали: "))
    print("Выберите желаемый цвет:\n1 - Белый\n2 - Синий\n3 - Желтый\n4 - Красный\n5 - Перламутровый\n6 - Серый металлик")
    try:
        color_num = int(input("Номер выбранного цвета: "))
    except ValueError:
        print("Можно вводить только числа")
    else:
        while not check.check_input(color_num, "color"):
            print("Введите число от 1 до 6")
            color_num = int(input("Номер выбранного цвета: "))
        cost = price.calculate_painting_cost(color_num, part) 
        print("Полученная цена:", int(cost), "рублей")


