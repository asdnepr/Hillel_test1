import json
# from pprint import pprint

# Задан файл HW.json
# Обработать исходный файл таким образом, чтобы получить получить результирующий файл по подобию НW_result.json.
# Весь код оформить в виде функций.
# Отчет содержит файлы:
# HW.json,
# *.py,
# изменений, в соответствии с исходными данными, НW_result.json.
# В задачи Ви примените: python функции, менеджер задач для для сериализации и десериализации данных,
# работа с json объектом, цикл for, условный оператор проверки типа данных, метод append для списка.
# 1. Загружаете исходный json
# 2. Преобразовываете его в словарь
# 3. Организовываете цикл для итерации исходного списка словарей
# 4. В списке словарей по ключам собираете полное ими персоны.
# 5. При помощи метода items из ключей и значений генерируете список кортежей пари ключ-значение.
# 6. По значению определяете тип и сортируете по типу согласно результирующему json-ну.
# 7. Генерируете все в новый словарь
# 8. Словарь записываете в новый файл.

with open('HW.json', 'r') as dict_data:
    text = json.load(dict_data)
my_list_int = []
my_list_str = []
my_list_float = []
my_list_none_type = []
my_list_bool = []
my_dict = {}
dict_data_dump = {}
dict_data_2 = {}
for item in text['employee']:
    personName = item['firstName'] + ' ' + item['lastName']
    for item_ in item.items():
        if isinstance(item_[1], bool):
            my_list_bool.append(item_[0])
        elif isinstance(item_[1], int):
            my_list_int.append(item_[0])
        elif isinstance(item_[1], str):
            my_list_str.append(item_[0])
        elif isinstance(item_[1], float):
            my_list_float.append(item_[0])
        elif isinstance(item_[1], type(None)):
            my_list_none_type.append(item_[0])
    my_dict["int"] = my_list_int.copy()
    my_dict["string"] = my_list_str.copy()
    my_dict["float"] = my_list_float.copy()
    my_dict["none_type"] = my_list_none_type.copy()
    my_dict["bool"] = my_list_bool.copy()
    my_list_int.clear()
    my_list_str.clear()
    my_list_float.clear()
    my_list_none_type.clear()
    my_list_bool.clear()
    dict_data_dump[personName] = my_dict.copy()
    my_dict.clear()
dict_data_2['employee'] = dict_data_dump
with open('HM_result.json', 'w') as f:
    json.dump(dict_data_2, f, indent=3)
# pprint(dict_data_2)
