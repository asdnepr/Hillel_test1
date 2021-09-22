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
# _____________________________________________________________________
# Задачу из “Homework 11. Paбота с json обектом.” перевести в формат ООП.
#
# Класс должен содержать атрибути и методи. Атрибутами будут пути к исходному и результирующему файлам.
# И как миниму 4 метода:
# конструктор должен на вход принимать возможние альтернативние варианти путей к исходному и результирующему файлам,
# но и иметь дефолтние значения, которими и будут отрибути класса;
# метод для загрузки исходного json обекта из исходного файла;
# метод для оброботки словаря полученного из исходного json обекта;
# метод для загрузки полученного результата в новий результирующий json файл.
# Если придумаете еще больше методов будет хорошо. Помните о принципе “Единственной ответственности”.
#
# Екземпляр класса визивать через определенную точку входа python скрипта.
import json
import os


class MyJsonClass:
    def __init__(self, original_path=os.getcwd(), result_path=os.getcwd()):
        self.result_ = {'employee': {}}
        self.original_path = original_path
        self.result_path = result_path
        self.update_()

    def original_file(self):
        with open('HW.json', 'r') as self.original_path:
            return json.loads(self.original_path.read())

    def update_(self):
        with open('HM_result.json', 'w') as new_json:
            new_json.write(self.result_json())

    @staticmethod
    def type_comparison(dict_):
        my_list_int = []
        my_list_str = []
        my_list_float = []
        my_list_none_type = []
        my_list_bool = []
        my_dict = {}
        for item_ in dict_.items():
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
        return my_dict

    def result_json(self):
        dict_data_dump = {}
        for item in self.original_file()['employee']:
            person_name = item['firstName'] + ' ' + item['lastName']
            dict_data_dump[person_name] = self.type_comparison(item)
        self.result_['employee'] = dict_data_dump
        return json.dumps(self.result_, indent=3)


if __name__ == '__main__':
    outcome = MyJsonClass()
