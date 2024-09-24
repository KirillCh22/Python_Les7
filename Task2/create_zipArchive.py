import os
import shutil
import zipfile
from zipfile import ZipFile


def zip_archive(path_directory: str, finish_zip: str):

    my_path_list = os.listdir(path_directory)
    print(my_path_list)

    # Коппируем данные из 1-ой задачи, чтобы их добавить в архив
    shutil.copytree(path_directory, "E:\Учеба в GeekBrains\Семинары по Python(углубленная)\Les7\Task2", dirs_exist_ok=True)


    # Создаем архив и добавляем в него файлы, по нынешнему пути
    with ZipFile(finish_zip, "w", compression=zipfile.ZIP_DEFLATED) as zpf:
        for zip_file in my_path_list:
            zpf.write(zip_file)


    # ПРОВЕРЯЕМ НА НАЛИЧИЕ СОЗДАНИЯ АРХИВА, ЕСЛИ АРХИВ СОЗДАН, ТО БУДЕТ FALSE
    check_zip_archive = os.path.isdir(finish_zip)
    if check_zip_archive == False:
        print("ZIP Archive Create")
    else:
        print("ERROR ZIP Archive not create")


def main():

    zip_archive(path_directory="E:\Учеба в GeekBrains\Семинары по Python(углубленная)\Les7\Task1",
                finish_zip="E:\Учеба в GeekBrains\Семинары по Python(углубленная)\Les7\Task2\zip_archive.zip")

if __name__ == '__main__':
    main()