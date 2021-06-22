# Задача 1
# Дано список словорей
# [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
# создать список кортежей
# [('red', 'high'), ('yellow', 'low')]
my_list = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
dict_1, dict_2 = my_list[0], my_list[1]
print(dict_1)
print(dict_2)
dict_1 = dict_1(key, )
# list_1, list_2, list_3, list_4 = list(dict_1.keys()), list(dict_2.keys()), list(dict_1.values()), list(dict_2.values())
# for i, r in list_1, list_2:
#     if list_1i) == list_2(r)

# d1 = {'a': [1, 2, 3], 'b': [5], 'c': [5, 6, 9]}
# d2 = {'a': [4], 'b': [8, 9, 0], 'd': [10, 14, 13]}
#
# list_1 = []
# output = {k: list_1.append(dict_1.get(k, [])) and list_1.append(dict_2.get(k)) for k in {*dict_1, *dict_2}}
# list_1 = tuple(output.values())
# tt = tuple(list_1)
# print(output)
# print(tt)

# list_1 = []
# for item in dict_1.items(), dict_2.items():
#     list_1.extend(item)
#     print(type(item))
# print(list_1)


# Dict1 = {'color': ['red'], 'value': ['high']}
# dict2 = {'color': ['yellow'], 'value': ['low']}
#
# # to store final result of dictionary
# result = []
#
# # iterate through each dictionary in list
# for dictionary in [dict_1, dict_2]:
#     # iterate through key value of dictionary items
#     for k, v in dictionary.items():
#         # if key is already in result dictionary then extend new values
#         result.extend(v)
#         # else if key is not in dictionary then add key with the first value
#
#
# print(result)
# Результат:
#
# {'d': [10, 14, 13], 'a': [1, 2, 3, 4], 'b': [5, 8, 9, 0], 'c': [5, 6, 9]}


# Задача 2
# Дано словарь
# a_dictionary = {"a": 1, "b": 2, "c": 3}
# преобразовать его в список кортежей
# [('a', 1), ('b', 2), ('c', 3)]


# Задача 3
# Дано два списка
# list_a = [1, 2, 3, 4]
# list_b = [5, 6, 7, 8]
# Создать из них список кортежей
# list_c = [(1,5), (2,6), (3,7), (4,8)]


# Задача 4
# Дано словарь
# {1:'entry 1', 2:'entry 2', 3:'entry 3', 4:'entry 4'}
# Создать кортеж занчений для первих трьох єлементов словоря


# Задача 5
# Дано список
# ["bar", "baz", "qux", "etc"]
# Создать кортеж
# ("foo", "bar", "baz", "qux", "etc")