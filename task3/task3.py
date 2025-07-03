import os
import json
os.chdir(os.path.dirname(__file__))  # Меняем директорию

while True:
    file1 = input("Пожалуйста, введите имя файла с тестами: ")
    if os.path.exists(file1):
         break
    print("Файл", file1, "отсутствует. Введите имя файла заново")

while True:
    file2 = input("Пожалуйста, введите имя файла со значениями: ")
    if os.path.exists(file2):
         break
    print("Файл", file2, "отсутствует. Введите имя файла заново")


# Загружаем первый JSON (основная структура)
with open(file1, "r") as f1:
    data1 = json.load(f1)

# Загружаем второй JSON (значения "value")
with open(file2, "r") as f2:
    data2 = json.load(f2)
    d_value = {entry["id"]: entry["value"] for entry in data2["values"]} # создём словарь


# Рекурсивная функция обхода со вставкой "value"
def values_recursively(node):
    if isinstance(node, dict):    # если словарь
        node_id = node.get("id")  # извлечь значение по ключу "id"
        if node_id in d_value:
            node["value"] = d_value[node_id]

        if "values" in node:         # Есть ли вложенные значения?
            for child in node["values"]:
                values_recursively(child) # вызываем рекурсивно

    elif isinstance(node, list):  # если список
        for item in node:
            values_recursively(item) # вызываем рекурсивно


# Запускаем на корневом списке тестов
values_recursively(data1["tests"])

# Сохраняем результат в новый файл
with open("report.json", "w", encoding="utf-8") as f3:
    json.dump(data1, f3, ensure_ascii=False, indent=2)

print("Значения сохранены в report.json.")
input("Нажмите Enter для выхода...")
