# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os

def split_file_path(file_path):
    path, full_filename = os.path.split(file_path)
    
    filename, file_extension = os.path.splitext(full_filename)
    
    return path, filename, file_extension

file_path = "/путь/к/файлу/имя_файла.txt"
path, filename, file_extension = split_file_path(file_path)

print("Путь:", path)
print("Имя файла:", filename)
print("Расширение файла:", file_extension)