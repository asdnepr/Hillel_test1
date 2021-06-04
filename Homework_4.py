# Создаю функцию для проверки на ошибку ввода, если введено не число
def int_value():
    # цикл до выполнения условия ввода целочисленного значения с последующим возвратом результата
    while True:
        my_value = input('Введите число: ')

        # проверка, что введено число
        try:
            my_value = int(my_value)

        # Если введено не целочисленное значение
        except ValueError:
            print("Ошибка ввода! Попробуйте еще раз.")

        # Вывод на печать и проверка типа
        else:
            print(my_value)
            print('type my_value: ', type(my_value))
            return my_value


# Создаю функцию для проверки на ошибку ввода, если введено не число/число с точкой
def float_value():
    # цикл до выполнения условия ввода целочисленного или дробного значения с последующим возвратом результата
    while True:
        my_value = (input('Введите число: '))

        # проверка, что введено число
        try:
            my_value = float(my_value)

        # Если введено не числовое значение
        except ValueError:
            print("Ошибка ввода! Попробуйте еще раз.")

        # Вывод на печать и проверка типа
        else:
            print(my_value)
            print('type my_value: ', type(my_value))
            return my_value


def float_fn(float_rez):
    return float(float_rez)


def str_fn(str_rez):
    return str(str_rez)


def int_fn(int_rez):
    return int(int_rez)


"""Задание 1. Создать python модуль для реализации ввода через клавиатуру целочисленних значений
Добавить функционал конвертации во float и str. Вывести результат на печать."""
# вызов функции
my_value_rez = int_value()
my_float_rez = float_fn(my_value_rez)
print(my_float_rez)
print('type my_float_rez: ', type(my_float_rez))
my_str_rez = str_fn(my_value_rez)
print(my_str_rez)
print('type my_str_rez : ', type(my_str_rez))


"""Задание 2. Создать python модуль для реализации ввода через клавиатуру дробных (с поавающей запятой) значений.
Добавить функционал конвертации во int и str. Вывести результат. на печать."""
my_value_rez2 = float_value()
my_int_rez2 = int_fn(my_value_rez2)
print(my_int_rez2)
print('type my_int_rez2: ', type(my_int_rez2))
my_str_rez2 = str_fn(my_value_rez2)
print(my_str_rez2)
print('type my_str_rez2 : ', type(my_str_rez2))
