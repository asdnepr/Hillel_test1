# 1. Организовываете точку входа.
# 2. В точке входа передаете главную функцию.

# 3. Создаете какую-то функцию some_func, которая будет принимать позиционные и поименованные аргументы
# (правильно организовать прием аргументов через args и kwargs). Эта функция должна поровну разделить все позиционные
# аргументы на списки с равным количеством элементов, чтобы хватило для всех ключей, и она же должна создать словарь,
# ключами которого будут поименованные аргументы, а значениями, получение ранее списки. Функция должна вернуть словарь

# 4. Создать еще одну функцию load_dict(some_dict, json_path), которая принимает словарь и путь к json файлу.
# Функция загружает словарь в соответствующий файл.

# 5. В главной функции вызываете, ранее созданную функцию some_func, передаете в нее 21 позиционный аргумент
# (21 задано специально, чтобы получить некратное значение) и 5 поименованных аргументов
# (имя аргумента равно самому значению ), пример, some_func(1,2,3,4,5, name = ‘name’, make = ‘make’).

# 6. Результаты функции some_func присваиваете какой-то переменной и прокидываете ее в функцию load_dict,
# в эту же функцию передаете и путь

# 7 Результат скрипт сгенерирует json файл, с соответствующим контентом, например {‘name’: [1, 2], ‘make’: [3, 4]}
import json


def main():
    pos_arg = list(range(1, 22))
    print(pos_arg)
    dict_args = some_func(*pos_arg, catfish="catfish", zander='zander', pike='pike', perch='perch', chub='chub')
    print(dict_args)
    load_dict(dict_args, "myjsonfile.json")
    return dict_args


def some_func(*args, **kwargs):
    print(args)
    print(kwargs)
    dict_args = {}
    print(len(args))
    print(len(kwargs))
    quotient = len(args) // len(kwargs)
    for i, key in enumerate(kwargs.keys()):
        dict_args.update({key: list(args[i*quotient: (i+1)*quotient])})
    return dict_args


def load_dict(some_dict, json_path):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(some_dict, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
