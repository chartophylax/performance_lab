import os
os.chdir(os.path.dirname(__file__))  # Меняем директорию на ту, в который расположен файл 2.py

file1 = input("введите имя файла с данными об окружности: ")
file2 = input("введите имя файла с данными о точках ")

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