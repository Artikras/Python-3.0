# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input())

if num == 1:
     print('x > 0, y > 0')
elif num == 2:
     print('x < 0, y > 0')
elif num == 3:
     print('x < 0, y < 0')
elif num == 4:
     print('x > 0, y < 0 ')
else:
     print('Такой четверти нет')

    # Еще вариант рещения через MATCH

quarter = input()

match quarter:
    case "1":
        print("x > 0, y > 0")
    case "2":
        print("x < 0, y > 0")
    case "3":
        print("x < 0, y < 0")
    case "4":
        print("x > 0, y < 0")
    case _:
        print("error")
        
