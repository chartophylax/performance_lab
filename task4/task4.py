import os
import sys

if len(sys.argv) < 2:
    print("Ошибка: Нет парамтров")
    input("Нажмите Enter для выхода...")
    sys.exit()

os.chdir(os.path.dirname(__file__))  # Меняем директорию
file=sys.argv[1]

if os.path.exists(file)==False:
    print("Ошибка: файл", file, "отсутствует")
    input("Нажмите Enter для выхода...")
    sys.exit()


nums = []
with open(file, "r") as file:
    for line in file:
        line = line.strip()  # убираем пробелы и перевод строки
        if line.isdigit() or (line.startswith('-') and line[1:].isdigit()):
            nums.append(int(line))  # добавляем в список

nums.sort()  # сортировка

# определяем медиану
n = len(nums)
if n % 2 == 1:
    median = nums[n // 2]
else:
    # при чётном количестве — берём большее из двух средних
    median = max(nums[n // 2 - 1], nums[n // 2])

# Шаг 3: считаем сумму модулей разности с медианой
total = sum(abs(num - median) for num in nums)

# Шаг 4: вывод

print("Минимальное количество ходов:", total)
input("Нажмите Enter для выхода...")