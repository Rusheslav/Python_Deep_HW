from pathlib import Path


def rename_files(path, new_name, original_extension, new_extension):
    p = Path(path)
    position = 0
    for file in p.iterdir():
        file_name = file.name
        original_name, extension = file_name.split('.')
        if extension == original_extension:
            position += 1
            new_file_name = f'{original_name}_{new_name}_{position}.{new_extension}'
            file.rename(f'{path}/{new_file_name}')
            print(f'Файл {file_name} переименован в {new_file_name}')
    print(f'\nВсего переименовано {position} из {len(list(p.glob("*")))} файлов в указанной папке')


rename_files('/Users/andrejlebedev/Documents/Geekbrains/Python_Deep_HomeWork/Test/test_directory', 'new_name', 'jpg', 'newext')
