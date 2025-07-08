import os
import sys

if len(sys.argv) < 3:
    print("Нужно передать два аргумента.")
    input("Заверешние. Нажмите Enter для выхода...")
    sys.exit()

file1 = sys.argv[1]
file2 = sys.argv[2]

os.chdir(os.path.dirname(__file__))  # Меняем директорию на папку скрипта

missing1 = not os.path.exists(file1)
missing2 = not os.path.exists(file2)

if missing1 or missing2:
    if missing1 and missing2:
        print(f"Ошибка. Файлы '{file1}' и '{file2}' отсутствуют.")
    elif missing1:
        print(f"Ошибка. Файл '{file1}' отсутствует.")
    elif missing2:
        print(f"Ошибка. Файл '{file2}' отсутствует.")
    input("Заверешние. Нажмите Enter для выхода...")
    sys.exit()


if os.path.exists(file1) and os.path.exists(file2):
    with open(file1, "r") as file:
        first_line = file.readline()
        parts1 = first_line.strip().split()

        if len(parts1) < 2:
            raise ValueError("В первой строке должно быть как минимум два числа.")

        x0 = float(parts1[0])
        y0 = float(parts1[1])

    # Cтрока с радиусом
        second_line = file.readline().strip()
        second_parts = second_line.split()
        if len(second_parts) != 1:
            raise ValueError("Во второй строке должно быть ровно одно число.")

        r = float(second_parts[0])

#    print(f"x0 = {x0}, y0 = {y0}, r = {r}")


    with open(file2, "r") as file:
        for line in file:
            parts2 = line.strip().split()
            if len(parts2) < 2:
#                print("Недостаточно данных в строке, пропуск...")
                continue

            x = float(parts2[0])
            y = float(parts2[1])
#            print(f"x = {x}, y = {y}")
        
            d = (x - x0)**2 + (y - y0)**2

            if round (d, 5) < round (r**2, 5):
                print(1)
            elif round (d, 5) > round (r**2, 5):
                print(2)
            else:
                print(0)
else:
       input("Имена файлов введены некорректно либо они недоступны: ")

input("Нажмите Enter, чтобы выйти...")