# Задача 1
# Дано список словорей
# [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
# создать список кортежей
# [('red', 'high'), ('yellow', 'low')]
my_list = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
# dict_1, dict_2 = my_list[0], my_list[1]
# dict_1 = {k: [v] for k, v in dict_1.items()}        #make a function
# dict_2 = {k: [v] for k, v in dict_2.items()}
# list_in_list = {k: dict_1.get(k, []) + dict_2.get(k, []) for k in {*dict_1, *dict_2}}
# tuples_in_list = list(list_in_list.values())
# tuples_in_list = [tuple(i) for i in tuples_in_list]
# print(tuples_in_list)
rez_list = [tuple(value.values()) for value in my_list]
print(rez_list)


# Задача 2
# Дано словарь
# a_dictionary = {"a": 1, "b": 2, "c": 3}
# преобразовать его в список кортежей
# [('a', 1), ('b', 2), ('c', 3)]
a_dictionary = {"a": 1, "b": 2, "c": 3}
print(list(a_dictionary.items()))


# Задача 3
# Дано два списка
# list_a = [1, 2, 3, 4]
# list_b = [5, 6, 7, 8]
# Создать из них список кортежей
# list_c = [(1,5), (2,6), (3,7), (4,8)]
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = list(zip(list_a, list_b))
# list_c = [(list_a[i], list_b[i]) for i in range(len(list_a))]
print(list_c)

# Задача 4
# Дано словарь
# {1:'entry 1', 2:'entry 2', 3:'entry 3', 4:'entry 4'}
# Создать кортеж занчений для первих трёх элементов словаря
my_dict = {1: 'entry 1', 2: 'entry 2', 3: 'entry 3', 4: 'entry 4'}
my_tuple = tuple(list(my_dict.values())[:3])
print(my_tuple)

# Задача 5
# Дано список
# ["bar", "baz", "qux", "etc"]
# Создать кортеж
# ("foo", "bar", "baz", "qux", "etc")
my_list_2 = ["bar", "baz", "qux", "etc"]
my_list_3 = ["foo"]
my_list_3.extend(my_list_2)
my_tuple_2 = tuple(my_list_3)
print(my_tuple_2)
