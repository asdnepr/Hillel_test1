# 1.Задан некоторый список A содержащий целые числа. Разработать программу, которая вычисляет сумму элементов списка.
A = [22, 33, 44, 55]
my_sum = 0
for i in A:
    my_sum += i
print(my_sum)

# 2.Задан список строк. В каждой строке подсчитать количество вхождений заданного символа
list_str = ['A mari usque ad mare.', 'Ab ovo usque ad mala.', 'Abiens abi!', 'Dictum est factum.']
st_2 = 0
my_input = input('Введите искомый символ: ')
for i in list_str:
    print(f"Вхождений символа '{my_input}' в строку '{list_str[st_2]}' - {list_str[st_2].count(my_input)} ")
    st_2 += 1

# 3.Пользователь вводит число. Определение наличия заданного элемента в списке
# list_=[2,8,3,4,3,5,2,1,0,3,4,4,5,8,7,7,5]. Если элемент не найден, то выводится соответствующее сообщение.
list_ = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
st_3 = 0
my_value = int(input('Введите число от 0 до 9: '))
while st_3 < len(list_):
    if my_value == list_[st_3]:
        print('Заданный элемент есть списке.')
        break
    else:
        st_3 += 1
else:
    print('Элемент не найден.')
