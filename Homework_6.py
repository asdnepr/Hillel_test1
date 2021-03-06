from random import randint

# Методы строк
test_txt = 'DIEC diem dOCeT.'
test_txt_2 = 'OOO AAA, OOO AA, OOO AAA, OOO'
"""capitalize()"""
# Возвращает копию строки в которой только первый символ находится в верхнем регистре, а все остальные в нижнем.
print(test_txt.capitalize())

"""casefold()"""
# Возвращает копию строки в которой все символы приводятся к нижнему регистру в соответствии с разделом
# 3.13 стандарта Юникода.
# Данная функция позволяет адаптировать программы к конкретным натуральным языкам
# (голландскому, греческому и т.д. см. таблицу), чего нельзя добиться с помощью метода lower():
print(test_txt.casefold())

"""center(width[, fillchar])"""
# Возвращает новую строку длинной width в которой исходная строка находится в центре,
# а справа и слева от нее находятся символы указанные в fillchar (по умолчанию пробел).
print(test_txt.center(45))

# В параметре fillchar можно указывать только один символ, а в случаях, когда количество необходимых
# для дополнения символов нечетно, справа их будет на 1 больше чем слева:
print(test_txt.center(20, 'q'))
print(test_txt.center(21, 'q'))

# Исходная строка возвращается без изменений, если width < len(test_txt):
print(test_txt.center(11, 'q'))

"""count(sub[, start[, end]])"""
# Возвращает количество вхождений строки sub в строке str.
print(test_txt_2.count('AA'))

# Подсчитываются только непересекающиеся последовательности символов
# Фактически, подсчет выполняется внутри среза [start : end], где start = 0 и end = None,
# что равносильно поиску по всей строке. Данные параметры интерпретируются как границы среза и
# могут принимать отрицательные значения:
#  Подсчет по всей строке:
print(test_txt_2.count('A'))

#  Подсчет в срезе [8:], равносильно .count('X', -21):
print(test_txt_2.count('A', 8))
print(test_txt_2.count('A', -21))

#  Подсчет в срезе [:8], равносильно .count('X', -30, -21):
print(test_txt_2.count('A', 0, 8))
print(test_txt_2.count('A', -29, -21))

#  Подсчет в срезе s[8:14], равносильно s.count('X', -22, -16)
print(test_txt_2.count('A', 8, 14))
print(test_txt_2.count('A', -21, -15))

"""encode(encoding="utf-8", errors="strict")"""
# Декодирует строку в указанную в параметре encoding кодировку и возвращает результат в виде строки типа bytes.
test_txt_3 = 'ПриветHello'

print(test_txt_3.encode(encoding='koi8_r'))

# Параметр errors позволяет определить необходимое поведение если декодирование невозможно:
#  декодирование невозможно: print(test_txt_3.encode(encoding='ascii')), поэтому -
#  игнорируем непереводимые символы:
print(test_txt_3.encode(encoding='ascii', errors='ignore'))

#  заменяем непереводимые символы на '?':
print(test_txt_3.encode(encoding='ascii', errors='replace'))

"""endswith(suffix[, start[, end]])"""

# Возвращает True если str заканчивается последовательностью символов suffix и False в противном случае.
print(test_txt_2.endswith('OO'))
# (True) все строки заканчиваются пустой строкой
print(test_txt_2.endswith(''))
test_txt_10 = ''
#  (True) даже пустые:
print(test_txt_10.endswith(''))

# Фактически, наличие конечных символов suffix определяется внутри среза [start : end],
# где start = 0 и end = None, что равносильно поиску по всей строке.
# Данные параметры интерпретируются как границы среза и могут принимать отрицательные значения
# срез [8:] оканчивается ' OOO AA, OOO AAA, OOO'
print(test_txt_2.endswith(' OOO AA, OOO AAA, OOO', 8))

# срез s[10:] оканчивается ' OOO AA, OOO AAA, OOO'
print(test_txt_2.endswith(' OOO AA, OOO AAA, OOO', 10))

# срез [1:5] оканчивается 'OO AA':
print(test_txt_2.endswith('AA', 1, 6))

# то же самое но с отрицательными индексами:
print(test_txt_2.endswith('AA', -28, -23))

"""expandtabs(tabsize=8)"""
# Разбивает строку по символам \t на столбцы указанной ширины.
test_txt_4 = '0\ta\tbb\tccc\tdddd\teeeee\tffffff'

print(test_txt_4.expandtabs())

# В данном примере все числа, находятся внутри столбцов шириной 8 символов. Но если какое-то значение
# не помещается внутри одного столбца, то ширина столбца будет увеличена в необходимое количество раз.
# Ширина столбцов может быть указана в параметре tabsize:
print(test_txt_4.expandtabs(20))

# Иногда, данный метод позволяет очень легко организовать вывод данных в виде выровненной таблицы:
for n in range(5):
    test_txt_5 = '\t'.join([str(randint(10, 100)) for i in range(5)])
    print(test_txt_5.expandtabs())

# Символы \n и \r остаются как есть, но не влияют на изменение ширины столбцов.

"""find(sub[, start[, end]])"""
# Возвращает индекс первого вхождения строки sub в строке.
print(test_txt_2.find('AA'))

# Если строка sub отсутствует внутри строки str то будет возвращена −1:
print(test_txt_2.find('AO'))

# Фактически, поиск выполняется внутри среза [start : end], где start = 0 и end = None,
# что равносильно поиску по всей строке. Данные параметры интерпретируются как границы среза и
# могут принимать отрицательные значения:
print(test_txt_2.find('AA', 8))
print(test_txt_2.find('AA', 8, 22))

"""format(*args, **kwargs)"""
# Данный метод позволяет вставить в указанные места указанные аргументы,
# с выполнением их предварительного форматирования. Места для вставки аргументов обозначаются фигурными скобками {},
# а в самих скобках указывается номер порядкового аргумента или имя именованного аргумента:
test_txt_6 = 'Возраст: {0}, Имя - {name}, Фамилия - {surname}'
print(test_txt_6.format(37, name='Artem', surname='Suhlobov'))
# После номера или имени аргумента, через двоеточие : может быть указан способ форматирования подставляемого значения

"""format_map(mapping)"""


# Тоже что и format(**mapping), но позволяет использовать собственные отображения (объекты типа "ключ - значение"),
# которые используются напряму, без копирования.


class MyMap(dict):
    def __missing__(self, key):
        return key


my_map = MyMap(a=1, b=2, c=3)
print('A = {a}; B = {b}; C = {c}; X = {x}'.format_map(my_map))


# Преимущества данной функции становятся заметны, когда мы указываем ключи которых нет в отображении.
# Например, когда мы указали ключ {x} которого не оказалось в my_map это не привело к ошибке.
# Но если мы попробуем проделать то же самое для метода format(), то это приведет к ошибке:
# >>> 'A = {a}; B = {b}; C = {c}'.format(**my_map)    #  ошибки нет
# 'A = 1; B = 2; C = 3'
# >>>
# >>> 'A = {a}; B = {b}; C = {c}; X = {x}'.format(**my_map)    #  ошибки есть
# KeyError: 'x'
# Дело в том, что когда мы используем метод format(**mapping) все отображение копируется в словарь,
# а когда мы используем format_map(mapping), то объект-отображение используется напрямую,
# вместе со всеми внутренними методами, включая __missing__():

class FlyMap(dict):
    def __missing__(self, key):
        return 'А лыжи сперли!'


test_txt_7 = 'Летим вверх на вертолете {plane}, а вниз катим на лыжах {ski}'
print(test_txt_7.format_map(FlyMap(plane='МИ-8')))

"""index(sub[, start[, end]])"""
# Аналогичен методу find, лиш с тем отличием, что вызывает исключение ValueError если строка sub не найдена.
print(test_txt_2.index('AA'))

"""isalnum()"""
# Возвращает True если строка не пустая и состоит только из букв и цифр.
print(test_txt_3.isalnum())
print(test_txt_2.isalnum())
# Но если в строке имеется хотябы один не буквенный и не числовой символ, то будет возвращено False:
# К буквам относятся все буквы Юникода, и не важно к какому языковому алфавиту эти буквы принадлежат

"""isalpha()"""
# Возвращает True если строка не пустая и состоит только из букв.
print(test_txt_3.isalpha())
print(test_txt_2.isalpha())
# Под буквой понимается любой алфавитный символ базы данных Юникода
# (точнее символы из категорий "Lm", "Lt", "Lu", "Ll" или "Lo")
print('\u00c0\u01a2\u01fe\u03e0'.isalpha())

"""isdecimal()"""
# Возвращает True если строка не пустая и состоит только из десятичных цифр.
test_txt_7 = '123456789'
print(test_txt_2.isdecimal())
print(test_txt_7.isdecimal())
# К цифрам относятся все символы Юникода, которые могут быть использованы для записи
# чисел в десятичной системе счисления (категория "Nd"), например, число
# 1234
#  в разных языках может выглядеть по разному:
#  ASCII:
test_txt_7_1 = '\u0031\u0032\u0033\u0034'
#  Деванагари:
test_txt_7_2 = '\u0967\u0968\u0969\u096a'
#  Кхмерский:
test_txt_7_3 = '\u17e1\u17e2\u17e3\u17e4'
# И все это цифры:
print(test_txt_7_1.isdecimal())
print(test_txt_7_2.isdecimal())
print(test_txt_7_3.isdecimal())

"""isdigit()"""
# Возвращает True если строка не пустая и состоит только из десятичных цифр и символов,
# которые так же отосятся к цифрам.
print(test_txt_2.isdigit())
print(test_txt_7.isdigit())
# Данный метод отличается от isdecimal() тем, что воспринимает символы,
# которые не могут участвовать в записи десятичных цифр, но при этом сами состоят из цифр,
# например, символы ², ³ являются показателями степени, но считаются цифровыми и возвращается True
# Фактически, данный метод вернет True для любого символа Юникода у которого свойство Numeric_Type
# равно Digit или Decimal


"""isidentifier()"""
# Возвращает True если строка является допустимым идентификатором языка Python.
# По сути, речь идет не о зарезервированных идентфикаторах – строках типа for и while),
# а о строках типа ValueError и False. Например:
# допустимый идентификатор:
print(test_txt_3.isidentifier())
# не допустимый идентификатор:
print(test_txt.isidentifier())
print(test_txt_2.isidentifier())
# В весьма поверхностном смысле, идентификаторы – это допустимые имена переменных, функций, классов и т.д.

"""islower()"""
# Возвращает True если строка не пустая и состоит только из алфавитных строчных букв.
print(test_txt_3.islower())
print(test_txt_3.casefold().islower())
# Фактически, речь идет о всех символах юникода со свойством "Ll":

"""isnumeric()"""
# Возвращает True если строка не пустая и состоит только из десятичных цифр и символов,
# которые так же отосятся к цифрам. Данный метод очень похож на методы isdecimal() и isdigit(),
# но возвращает True так же для цифровых символов чье свойство Numeric_Type равно Numeric. Например, символ ¾:
print('\u00be'.isnumeric())
print('\u00be'.isdigit())
print('\u00be'.isdecimal())

"""isprintable()"""
# Возвращает True если все символы в строке являются печатаемыми или если строка является пустой.
# Некоторые символы, например, такие как символ "разделитель файлов",
# являются непечатаемыми и служат для других целей. В чем очень легко убедиться:
test_txt_8 = '\u001c'
print(test_txt_8)
print(test_txt_8.isprintable())
# все символы Юникода из категорий "Other" и "Separator" считаются непечатаемыми. Кроме ASCII пробела:
print(test_txt_2.isprintable())
# А вот некоторые экранированные последовательности считаются непечатаемыми:
test_txt_9 = 'непечатаемый\nсимвол'
print(test_txt_9.isprintable())
# метод вернет True если строка пуста:
print(test_txt_10.isprintable())

"""isspace()"""
# Возвращает True если строка не пуста и состоит только из пробельных символов, в противном случае возвращается False.
print(test_txt_10.isspace())
test_txt_11 = '           '
print(test_txt_11.isspace())
# Под пробельными символами могут пониматься все символы Юникода из категорий "Other" и "Separator",
# например, символ "разделитель файлов" так же считается пробельным, даже несмотря на то, что он является непечатаемым:
print(test_txt_8.isspace())

"""istitle()"""
# Возвращает True если строка не пустая и является строкой заголовков (см. title()).
test_txt_12 = 'Здрасте Приехали!'
print(test_txt_3.istitle())
print(test_txt_12.istitle())

"""isupper()"""
# Возвращает True если строка не пустая и все символы находятся в верхнем регистре (см. upper()),
# В строке могут присутствовать пробелы:
print(test_txt_2.isupper())
print(test_txt.isupper())

"""join(iterable)"""
# Возвращает новую строку, которая является объединением (конкатенацией) строк из итерируемого объекта iterable
# через разделитель str.
print(test_txt_11.join([test_txt, test_txt_3, test_txt_7]))
# Если какое-то значение в iterable не является стрококй, то это приведет к ошибке
# Если в iterable находятся нестроковые значения, но все равно необходимо их объединить в строку,
# то для преобразования всех элементов в строку можно воспользоваться функцией str() либо в генераторе:
test_txt_13 = [1, 2, 3, 4, 5]
print(test_txt_11.join([str(i) for i in test_txt_13]))
# Либо отобразить функцию str() на iterable с помощью функции map():
print(test_txt_11.join(map(str, test_txt_13)))

"""ljust(width[, fillchar])"""
# Возвращает новую строку в которой исходная строка str дополнена справа символами fillchar
# (по умолчанию это пробел ASCII) до указанной длины width.
print(test_txt.ljust(30))
print(test_txt.ljust(30, 'O'))
# Параметр fillchar может быть только одним символом, а не произвольной строкой:
# Если width < len(str) то указанная строка возвращается без изменений:

"""lower([chars])"""
# Возвращает новую строку в которой все символы исходной строки преобразованы к нижнему регистру
# в соответствии с разделом 3.13 стандарта Юникода.
print(test_txt.lower())

"""lstrip([chars])"""
# Возвращает копию исходной строки в которой слева удалены указанные символы
# (по умолчанию удаляются пробельные символы).
print(test_txt.lstrip())
# В параметре chars может быть указана последовательность символов, которые необходимо удалить слева:
print(test_txt.lstrip('DIE'))
test_txt_14 = 'xxxyyyzzz'
print(test_txt_14.lstrip('x'))
print(test_txt_14.lstrip('xy'))
print(test_txt_14.lstrip('xyz'))
# Последовательность символов в chars не имеет никакого значения.
# Если какой-то символ в ее составе найден слева в строке str, то он будет удален:
print(test_txt_14.lstrip('zyx'))

"""maketrans(x[, y[, z]])"""
# Возвращает таблицу преобразования символов, используемую методом translate().
# Содержание строки, относительно которой вызывается метод maketrans() не имеет никакого значения.
# Если методу передается всего один аргумент, то это должен быть словарь,
# отображающий одни единичные символы Юникода в другие:
my_table = test_txt_10.maketrans({'a': '1', 'b': '2', 'c': '3'})
test_txt_21 = 'a___b___c'
print(test_txt_21.translate(my_table))
# Если передаются два аргумента, то это должны быть строки одинаковой длины, причем символы первой строки
# отображаются на соответствующие символы второй:
my_table_2 = test_txt_10.maketrans('abc', '123')
print(test_txt_21.translate(my_table_2))
# Третьим аргументом может быть строка, символы которой изключаются из строки,
# относительно которой вызван метод translate():
my_table_3 = test_txt_10.maketrans('abc', '123', '_#*')
test_txt_22 = 'a_*#*_b_*#*_c'
print(test_txt_22.translate(my_table_3))
# Данный метод позволяет использовать все экранированные последовательности для работы с символами
# Юникода: \xhh, \ooo, \N{id}, \uhhhh, \Uhhhhhhhh.

"""partition(sep)"""
# Разбивает строку по указанному разделителю и возвращает кортеж из трех элементов: строка до разделителя,
# сам разделитель и строка после разделителя.
test_txt_15 = 'qqqq1wwww'
print(test_txt_15.partition('1'))
# Если разделитель не найден, то возвращается кортеж так же состоящий из трех элементов в котором первый элемент
# – это исходная строка, а два других элемента – это пустые строки.
print(test_txt_15.partition('2'))

"""replace(old, new[, count])"""
# Возвращает копию исходной строки в которой все подстроки old заменены на подстроки new.
# Параметр count позволяет указать количество замен.
print(test_txt_2.replace('OO', 'X'))
# Параметр count позволяет указать необходимое количество замен:
print(test_txt_2.replace('OO', 'X', 2))

"""rfind(sub[, start[, end]])"""
# Возвращает индекс последнего вхождения подстроки sub в строке.
print(test_txt_2.rfind('AA'))
print(test_txt_2.rfind('O'))
# Фактически, поиск выполняется внутри среза [start : end], где start = 0 и end = None,
# что равносильно поиску по всей строке.
# Данные параметры интерпретируются как границы среза и могут принимать отрицательные значения:
print(test_txt_2.rfind('O', 3))
print(test_txt_2.rfind('O', 3, 15))
# Обратить внимание на то, что хоть поиск строки и выполняется внутри среза,
# но возвращаемый индекс вычисляется относительно всей длины исходной строки.
# Если не найдено ни одного вхождения то возвращается -1:
print(test_txt_2.rfind('OA', 3, 15))

"""rindex(sub[, start[, end]])"""
# Выполняет тоже самое, что и метод rfind(), но в случае если не найдено ни одного вхождения подстроки
# он вызывает исключение ValueError, а не возвращает -1.
print(test_txt_2.rindex('OO'))

"""rjust(width[, fillchar])"""
# Возвращает новую строку в которой исходная строка дополнена слева указанным в параметре width количеством
# символов fillchar (по умолчанию – это пробел).
print(test_txt_3.rjust(25))
print(test_txt_3.rjust(25, 'E'))
# Параметр fillchar может быть только единичным символом, а не произвольной строкой
# Если width < len(str), то будет возвращена исходная строка без изменений:
print(test_txt_3.rjust(5))

"""rpartition(sep)"""
# Разбивает строку по последнему встреченному разделителю sep и возвращает кортеж,
# который состоит из трех элементов: строки до разделителя, самого разделителя и строки после разделителя.
test_txt_23 = 'aa_x_bb_x_cc_x_dd'
print(test_txt_23.rpartition('_x_'))
# Если разделитель в строке отсутствует, то кортеж будет состоять из: двух пустых строк и исходной строки:
print(test_txt_23.rpartition('_Y_'))

"""rsplit(sep=None, maxsplit=-1)"""
# Аналогичен методу split() с тем лишь отличием, что если параметр maxsplit указан,
# то разбиение выполняется справа налево.
test_txt_24 = '1 2 3 4 5 6 7'
print(test_txt_24.rsplit(maxsplit=3))
test_txt_25 = '1->2->3->4->5->6'
print(test_txt_25.rsplit('->', maxsplit=3))
print(test_txt_24.split(maxsplit=3))

"""rstrip([chars])"""
# Аналогичен методу lstrip(), но удаление удаление пробелов или указанных символов chars происходит справа а не слева.
test_txt_26 = '   xxx   '
print(test_txt_26.rstrip())
print(test_txt_26.lstrip())
test_txt_27 = 'abcxxxabc'
print(test_txt_27.rstrip('cba'))
print(test_txt_27.lstrip('cba'))

"""split(sep=None, maxsplit=-1)"""
# Выполняет разбиение исходной строки на подстроки по символу пробела и возвращает их в виде списка.
print(test_txt_24.split())
# Параметр sep позволяет указать необходимый разделитель:
print(test_txt_25.split('->'))
# Однако, если параметр sep задан, то следующие друг за другом разделители не воспринимаются как один и
# считаются разделителями пустых строк:
test_txt_28 = '1, , , 4, , , 5'
print(test_txt_28.split(', '))

test_txt_29 = '1-->-->4-->-->5'
print(test_txt_28.split('-->'))
# пробелы объединяются:
test_txt_40 = '1      4      5'
print(test_txt_40.split())
# Если параметр sep не указан или равен None, то последовательные пробелы, будь они вначале,
# внутри или в конце строки объединяются вместе и вообще исключаются из разбиений:
test_txt_30 = '   1   2   3   '
print(test_txt_30.split())
# Если строка состоит только из пробелов или является пустой, то результатом разделения по пробелу будет пустой список
# Но разделение пустой строки любым разделителем, отличным от пробела, вернет список с пустой строкой
# По умолчанию Параметр maxsplit позволяет указать необходимое количество разбиений,
# которые будут выполнены слева направо:
print(test_txt_24.split(maxsplit=3))
print(test_txt_25.split('->', 3))
# При этом в списке будет присутствовать maxsplit + 1 элементов.
# По умолчанию, maxsplit = -1, что соответствует разбиению по всем присутствующим разделителям.


"""splitlines([keepends])"""
# Разбивает строку на подстроки по фиксированному набору разделителей и возвращает их в списке.
# В отличие от метода split() в котором можно указать произвольный разделитель,
# в методе splitlines набор разделителей является фиксированным:
# \n — перенос строки;
# \r — возврат каретки;
# \r\n — возврат каретки и перенос строки;
# \v or \x0b — вертикальный отступ;
# \f or \x0c — разрыв страницы;
# \x1c — разделитель файлов;
# \x1d — разделитель групп;
# \x1e — разделитель строк;
# \x85 — следующая строка;
# \u2028 — разделитель строк;
# \u2029 — разделитель абзацев.
test_txt_31 = 'A AA\nB BB\rC CC\vD DD'
print(test_txt_31.splitlines())
# Символ пробела не считается разделителем по умолчанию, как в методе split().
# Параметр keepends, установленный в значение True (по умолчанию False) позволяет включать разделители в подстроки:
print(test_txt_31.splitlines(keepends=True))
# Для пустой строки метод вернет пустой список:
print(test_txt_10.splitlines())
# Если в конце строки присутствует всего единственный разделитель, то он просто исключается из нее
# Однако, последовательно идущие разделители не объединяются вместе, а считаются разделителями пустых строк

"""startswith(prefix[, start[, end]])"""
# Возвращает True если строка str начинается с последовательности символов prefix (префикса) и False в противном случае.
test_txt_32 = 'Есть ли тут префикс???'
print(test_txt_32.startswith('Ес'))
# Параметр prefix может принимать не только один префикс, но и целый кортеж префиксов и если хоть один из них будет
# найден в начале строки, то мы так же получим True:
print(test_txt_32.startswith(('Ес', 'ту', 'пре')))
# Параметры start и end позволяют задать границы среза строки str и могут принимать отрицательные значения:
print(test_txt_32.startswith('ту'))
print(test_txt_32.startswith('ту', 8))
print(test_txt_32.startswith('ту', -14))
print(test_txt_32.startswith('ту', 8, 11))

"""strip([chars])"""
# Возвращает копию исходной строки в начале и конце которой удалены указанные символы chars.
# Если параметр chars не указан, то по умолчанию удаляются пробельные символы.
print(test_txt_27.strip('abc'))
# Символы в параметре chars рассматриваются не как последовательность, а как набор символов, которые необходимо удалить:
#
test_txt_33 = 'ccbacb_XXX_baacabb'
print(test_txt_23.strip('bca'))

"""swapcase()"""
# Возвращает копию исходной строки в которой все заглавные буквы преобразованы в строчные, строчные – в заглавные.
print(test_txt.swapcase())
# В редких случаях, из-за особенностей преобразования к верхнему или нижнему регистру некоторых символов Юникода
# может произойти так, что str == str.swapcase().swapcase() вернет False. Но, это действительно – редкость.

"""title()"""
# Возвращает строку в которой каждое слово исходной строки начинается с буквы в верхнем регистре,
# а все остальные буквы в нижнем.
print(test_txt.title())
# Под словом понимается любая последовательность букв разделенная небуквенными символами
print(test_txt_4.title())
# Что в некоторых ситуациях может быть не желательным, например:
test_txt_16 = "let's go"
print(test_txt_16.title())
# В таких ситуациях лучше всего воспользоваться модулем re.


"""translate(table)"""
# Преобразует символы исходной строки в соответствии с правилами преобразования в объекте table.
# Проще всего данный метод использовать в связке с методом .maketrans(),
# позволяющим быстро задать таблицу преобразований:
my_table = test_txt_10.maketrans('abc', '123', '_#*')
test_txt_20 = 'a_*#*_b_*#*_c'
print(test_txt_20.translate(my_table))

"""upper()"""
# Возвращает новую строку в которой каждый символ строки находится в верхнем регистре.
print(test_txt.upper())
# Символы, которые не могут быть приведены к верхнему регистру остаются без изменений
# Как правило, с этим преобразованием, не связано никаких проблем, но следует иметь в виду,
# что в очень редких случаях символы могут быть преобразованы не к верхнему регистру (категория "Lu"),
# а к прописным (категория "Lt"). Поэтому метод isupper() может выдавать False, когда от него ожидается True.
# Если вы все-таки с этим столкнулись, то смотрите документацию по преобразованию к верхнему регистру
# на официальном сайте Юникода.

"""zfill(width)"""
# Возвращает новую строку, в которой исходная строка дополнена нулями слева, так что бы длина новой строки
# стала равна width.
print(test_txt_7.zfill(15))
# Обратить внимание на то, что в параметре width указывается не количество нулей,
# а именно длина результирующей строки, если width < len(str), то исходная строка возвращается без изменений:
print(test_txt_7.zfill(8))
#  width указывает необходимую длину строки:
print(len('3.14'.zfill(20)))
# Знаки "+" и "-" всегда располагаются в начале строки и учитываются при расчете длины
