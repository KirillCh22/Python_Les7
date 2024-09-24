import os


def searching_files_by_extensions(path: str, extension: str):

    finding_files = list()
    for address, dirs, files in os.walk(path):
        for file in files:
            #file_path = os.path.join(address, file)
            finding_files.append(file) if file.endswith(extension) else finding_files.append("")


    return finding_files


def main():

    check_files_path = "E:\Учеба в GeekBrains\Семинары по Python(углубленная)\Les7\Task2"
    extension = ".py"

    finding_files = list(searching_files_by_extensions(path=check_files_path, extension=extension))

    print(finding_files)

if __name__ == '__main__':
    main()