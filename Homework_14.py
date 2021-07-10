# Декораторы:
# Создать функцию для генерации списка словарей вида
# [{0:0,}, {0:0, 1:1}, {0:0, 1:1, 2:4}, {0:0, 1:1, 2:4, 3:9}, {0:0, 1:1, 2:4, 3:9, ... n: n**2}, ]
# где n – именованный аргумент функции.
# Функция будет использовать цикл for, внутри которой при помощи Dict Comprahansion будут генерироваться
# вложенные словари. Запись в результирующий список производиться при помощи метода append.
# Создать декоратор для вычисления времени выполнения функци. Для создания декоратора использовать модуль datetime.
# Результатом вызова функции должен быть вывод самого списка и продолжительности выполнения генерирования списка.
# Функциональное программирование:
# Дано 3 списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# Используя методи функционального програмирования:
# 1. Из первого и третьего списков оставить все четные числа;
# 2. Со второго оставить все нечетные;
# 3. Объединить списки в один список кортежей пар (значение первого списка, значение второго списка,
# значение третьего списка);
# 4. По каждому кортежу определить сумму его значений, получите список сумм кортежей;
# 5. После получения списка п.4 оставить в нем только нечетные значения.
#
# Код оформить в виде функций.
# Код должен быть максимально автоматизирован!
import datetime
import random


def decorator_datetime(function):
    def wrapper(n):
        start_time = datetime.datetime.now()
        function(n)
        print(f"Время выполнения: ", datetime.datetime.now() - start_time)
    return wrapper


@decorator_datetime
def gen_list_dict(n):
    my_list = []
    for a in range(n+1):
        my_dict = {num: num ** 2 for num in range(a + 1)}
        my_list.append(my_dict)
    print(my_list)


def even_number(list_):
    list_t = []
    for i in list_:
        if i % 2 == 0:
            list_t.append(i)
    return list_t


def odd_number(list_):
    list_t = []
    for i in list_:
        if i % 2 != 0:
            list_t.append(i)
    return list_t


def main():
    gen_list_dict(n=random.randint(30, 100))
    return gen_list_dict


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


list_1, list_3 = even_number(list_1), even_number(list_3)
list_2 = odd_number(list_2)
print(list_1, list_2, list_3)
list_4 = list(zip(list_1, list_2, list_3))
sum_tuple = list(map(sum, list_4))
print(sum_tuple)


if __name__ == '__main__':
    main()
