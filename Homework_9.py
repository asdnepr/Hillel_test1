import string
import random


def test_print(x):
    print(id(x))
    print(x)


# Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами первый и последний элемент объекта.
# Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
# Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
my_dict = {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3', 'key_4': 'value_4', 'key_5': 'value_5'}
test_print(my_dict)
# Меняем местами первый и последний элемент объекта
first, last = list(my_dict.items())[0], list(my_dict.items())[-1]
my_list = list(my_dict.items())
my_list[0], my_list[-1] = last, first
my_dict.clear()
for my_key, my_value in my_list:
    my_dict[my_key] = my_value
test_print(my_dict)
# # Удаляем второй элемент
second = list(my_dict.items())[1]
del my_dict[second[0]]
test_print(my_dict)
# Вставляем новый элемент
my_dict['new_key'] = 'new_value'
test_print(my_dict)

# Как получить значение по ключу "marks" словаря student = {"name": "Emma", "class": 9, "marks": 75}
student = {"name": "Emma", "class": 9, "marks": 75}
print(student['marks'])
# Что выведет этот код? p = {"name": "Mike", "salary": 8000} print(p.get("age")).
p = {"name": "Mike", "salary": 8000}
print(p.get("age"))
# Код выведет - None

# Как получить "d":sample = {"1":["a","b"], "2":["c","d"]}.
sample = {"1": ["a", "b"], "2": ["c", "d"]}
print(list(sample.items())[1][1][1])
# Дан список стран и городов каждой страны. Затем дан список названия городов. Для каждого города укажите,
# в какой стране он находится.
# list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"],
# list_2 = ["Киев", "Токио", "Минск"] Получить dict_ = ["Украина": "Киев", "Япония": "Токио", "Беларусь": "Минск"]
list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
list_2 = ["Киев", "Токио", "Минск"]
dict_ = {}
for item in list_1:
    splitted_item = item.split('-')
    if splitted_item[1] in list_2:
        word_type = splitted_item[1]
        word = splitted_item[0]
        dict_[word] = word_type
print(dict_)
# Для английского алфавита сгенерировать словарь-шифратор, то есть словарь, где ключ буква алфавита,
# а значение являются случайное значение. Используя словарь, зашифровать/расшифровать введенное сообщение.
# string.ascii_lowercase
ang = dict([(character, random.randint(1000, 9999)) for character in string.ascii_lowercase])
print(ang)
result = []
result_2 = []
message = input("Введите сообщение: ")
message = list(message)
# Получение соответствий цифр для букв.
for symbol in message:
    for key in ang:
        if key == symbol:
            result.append(ang[key])
print(result)
gna = []
for i in ang.keys():
    gna.append((ang[i], i))
ang_r = dict(gna)
print(ang_r)
for symbol in result:
    for key in ang_r:
        if key == symbol:
            result_2.append(ang_r[key])
print(*result_2)
# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
my_dict_2 = {}
for i in (range(1, 10)):
    my_dict_2 [i] = i**3
print(my_dict_2)
# Создайте словарь из строки следующим образом: в качестве ключей возьмите буквы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку.
my_dict_3 = {}
my_str = input("Введите строку: ")
for i in my_str:
    my_dict_3[i] = my_str.count(i)
print(my_dict_3)
