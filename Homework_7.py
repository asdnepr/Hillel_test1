import random


# 1.Задан некоторый список A содержащий целые числа. Разработать программу, которая вычисляет сумму элементов списка.

def random_value():
    random_val = random.randrange(1, 10, 1)
    return random_val


def int_value():
    while True:
        my_value = input('Введите число от 0 до 9: ')

        try:
            my_value = int(my_value)

        except ValueError:
            print("Ошибка ввода! Попробуйте еще раз.")

        else:
            return my_value


my_list = [random_value() for i in range(random_value())]
st_1 = 0
my_sum = 0
while st_1 < len(my_list):
    my_sum += my_list[st_1]
    st_1 += 1
print(f"Сумма элементов списка {my_list} равна: {my_sum}")

# 2.Задан список строк. В каждой строке подсчитать количество вхождений заданного символа
list_str = ['A mari usque ad mare.', 'Ab ovo usque ad mala.', 'Abiens abi!', 'Dictum est factum.']
st_2 = 0
my_input = input('Введите искомый символ: ')
while st_2 < len(list_str):
    print(f"Вхождений символа '{my_input}' в строку '{list_str[st_2]}' - {list_str[st_2].count(my_input)} ")
    st_2 += 1

# 3.Пользователь вводит число. Определение наличия заданного элемента в списке
# list_=[2,8,3,4,3,5,2,1,0,3,4,4,5,8,7,7,5]. Если элемент не найден, то выводится соответствующее сообщение.

list_ = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
st_3 = 0
my_value = int_value()
while st_3 < len(list_):
    if my_value == list_[st_3]:
        print("Заданный элемент есть списке.")
        break
    else:
        st_3 += 1
else:
    print("Элемент не найден.")

