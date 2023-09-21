# Напишите следующие функции:
# 1. Нахождение корней квадратного уравнения
# 2. Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# 3. Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# 4. Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


import csv
import json
import math
import random

# 1.Функция для нахождения корней квадратного уравнения
def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root1 = root2 = -b / (2*a)
        return root1,
    else:
        return None

# 2. Функция для генерации CSV файла с тремя случайными числами в каждой строке
def generate_random_csv(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for _ in range(num_rows):
            row = [random.randint(1, 1000) for _ in range(3)]
            csv_writer.writerow(row)

# 3. Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из CSV файла
def run_quadratic_roots_with_csv(func):
    def wrapper(filename):
        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                try:
                    a, b, c = map(int, row)
                    result = func(a, b, c)
                    print(f"Input: a={a}, b={b}, c={c}, Result: {result}")
                except ValueError:
                    print(f"Skipping invalid row: {row}")
    return wrapper

# 4. Декоратор, сохраняющий переданные параметры и результаты работы функции в JSON файл
def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            data = {
                "parameters": args,
                "result": result
            }
            with open(filename, 'w') as jsonfile:
                json.dump(data, jsonfile, indent=4)
            return result
        return wrapper
    return decorator

# Создайте CSV файл с тремя случайными числами в каждой строке
generate_random_csv('random_numbers.csv', 100)

# Примените декораторы к функции нахождения корней квадратного уравнения
@run_quadratic_roots_with_csv
@save_to_json('results.json')
def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root1 = root2 = -b / (2*a)
        return root1,
    else:
        return None

# Запустите функцию с CSV файлом
quadratic_roots('random_numbers.csv')
