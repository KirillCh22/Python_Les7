import os
import time


def check_and_remove_old_file(path: str, count_days: int):

    days_in_sec = count_days * 86400
    real_time = time.time()
    limit_time = real_time - days_in_sec

    time_life_file = list()


# ПРОХОД ПО ВСЕМ ФАЙЛАМ В ДИРЕКТОРИИ LES7\TASK1
# СМОТРИМ ИХ ВРЕМЯ СОЗДАНИЯ И ПОСЛЕДНЕЕ ИЗМЕНЕНИЯ ОТ НАЧАЛА UNIX
# ЗАТЕМ СРАВНИВАЕМ ИХ РАЗНИЦУ С НАШЕМ ОГРАНИЧЕНИЕМ ПО ВРЕМЕНИ и В СЛУЧАЕ
# ЧЕГО УДАЛЯЕМ ФАЙЛ ИЗ ДИРЕКТОРИИ
    for address, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(address, file)
            time_into_unix = os.path.getmtime(file_path)
            time_life_file.append(time_into_unix)
            time_classic = time.ctime(time_into_unix)

            if time_into_unix - limit_time > 200000000:
                os.remove(file_path)
                print(f"Удален файл: {file_path}")
            else:
                print("Пока нечего удалять, все файлы свежие!")

            print(file_path)
            print(f"От UNIX - {time_into_unix}, в классическом виде - {time_classic} \n")



def main():

    check_path = "E:\Учеба в GeekBrains\Семинары по Python(углубленная)\Les7\Task1"

    check_and_remove_old_file(path=check_path, count_days=30)


if __name__ == '__main__':
    main()