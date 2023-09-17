# ✔Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п. 
# ✔Каждая группа включает файлы с несколькими расширениями. 
# ✔В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import shutil

def sort_files_by_extension(source_folder, destination_folder):
    file_extensions = {
        'Изображения': ['.jpg', '.jpeg', '.png', '.gif'],
        'Видео': ['.mp4', '.avi', '.mkv'],
        'Текст': ['.txt', '.doc', '.pdf'],
    }

    for folder_name in file_extensions.keys():
        folder_path = os.path.join(destination_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    for filename in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, filename)

        if not os.path.isfile(source_file_path):
            continue

        file_extension = os.path.splitext(filename)[1].lower()

        destination_folder_name = None
        for folder_name, extensions in file_extensions.items():
            if file_extension in extensions:
                destination_folder_name = folder_name
                break

        if destination_folder_name:
            destination_folder_path = os.path.join(destination_folder, destination_folder_name)
            shutil.move(source_file_path, os.path.join(destination_folder_path, filename))

if __name__ == "__main__":
    source_folder = "C:\gb\hw7\sf"   #"путь к исходной папке"
    destination_folder = "C:\gb\hw7" #"путь к целевой папке"

    sort_files_by_extension(source_folder, destination_folder)