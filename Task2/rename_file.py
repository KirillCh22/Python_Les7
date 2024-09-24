import random
import os

def _find_random_number(number: int):

    # МЕТОД ПО ПОЛУЧЕНИЕ РАНДОМНОГО ЧИСЛА ИСХОДЯ ИЗ ТОГО, КАКАЯ РАЗРЯДНОСТЬ ВВЕДЕНА ПОЛЬЗОВАТЕЛЕМ
    match number:
        case 1:
            return random.randint(1, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)
        case 4:
            return random.randint(1000, 9999)
        case 5:
            return random.randint(10000, 99999)

def group_rename_file(desire_finish_name: str, count_numbers_in_sequence_number: int, extensions_of_source_file: str,
                      extensions_of_finish_file: str, range_save_origin_name: str):


    # РАЗБИВАЕМ ДИАПАЗОН ДЛЯ УСТАНОВКИ МИНИМУМА И МАКСИМУМА
    range_user = list(range_save_origin_name.split(','))
    start_range = int(range_user[0])
    stop_range = int(range_user[1])

    print(f"{start_range}, {stop_range}")

    my_path = os.listdir()
    print(my_path)

    # УКАЗАНИЕ НАЧАЛЬНОГО РАСШИРЕНИЯ ФАЙЛА
    extension = (extensions_of_source_file)
    need_file = []

    # Добавление в новый список нужных файлов С ЗАДАННЫМ РАСШИРЕНИЕМ
    for item in my_path:
        need_file.append(item) if item.endswith(extension) else print("Nothing append")

    print(need_file)

    # ДОБАВЛЕНИЕ В НОВЫЙ СПИСОК ТОЛЬКО ИМЕНИ ФАЙЛА БЕЗ РАСШИРЕНИЯ
    str_name = []
    for name in range(len(need_file)):
        name = need_file[name]
        str_name.append(name[:4])

    print(str_name)

    # ДОБАВЛЕНИЕ К ИМЕЮЩЕМУСЯ ИМЕНИ, НОВОЕ ИМЯ + НОВЫЙ НОМЕР И НОВОЕ РАСШИРЕНИЕ ФАЙЛА
    for rename_files in range(len(str_name)):
        if len(str_name[rename_files]) < stop_range:
            str_name[rename_files] += desire_finish_name
            str_name[rename_files] += str(_find_random_number(count_numbers_in_sequence_number))
            str_name[rename_files] += extensions_of_finish_file
        else:
            print("Пока ничего, когда больше длинны")

    print(str_name)

    # ПОЛУЧЕНИЕ ФАЙЛОВ ПО ДАННОМУ ПУТИ И ПРОВЕРКА ДАННОГО ПУТИ НА АКУТАЛЬНОСТЬ
    check_path = os.path.isdir("/")
    if check_path == True:  # ЕСЛИ ТАКОЙ ПУТЬ СУЩЕСТВУЕТ, ТО МЫ МЕНЯЕМ СТАРЫЕ ИМЕНА ФАЛОВ НА НОВЫЕ

        for rename in range(len(str_name)):
            os.rename(need_file[rename], str_name[rename])

    else:    # ИНАЧЕ ПРОСТО ОШИБКА
        print("False")

    print(my_path)


def main():

    user_finish_name_file = input("Введите желаемое конечное имя файла: ")
    user_count_numbers_in_file = int(input("Введите количество цифр в порядковом номере: "))
    user_extensions_of_source_file = input("Введите расширение для исходного файла: ")
    user_extensions_of_finish_file = input("Введите расширение для конечного файла: ")
    user_range_save_orogin_name = input("Введите диапазон для сохранения оригинального имени, диапазон укажите через ',' : ")

    group_rename_file(user_finish_name_file, user_count_numbers_in_file, user_extensions_of_source_file,
                      user_extensions_of_finish_file, user_range_save_orogin_name)


if __name__ == '__main__':
    main()

