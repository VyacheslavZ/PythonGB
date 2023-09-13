# Напишите функцию в шахматный модуль. 
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random
from hw2 import are_queens_safe

def generate_random_queens(): # генерирует случайную расстановку 8 ферзей
    queens = []
    while True:
        queens = [(random.randint(1, 8), random.randint(1, 8)) for _ in range(8)]
        if are_queens_safe (queens):
            return queens

def print_chessboard(queens):
    chessboard = [['.' for _ in range(8)] for _ in range(8)]
    for x, y in queens:
        chessboard[y-1][x-1] = 'Q'

    for row in chessboard:
        print(' '.join(row))

if __name__ == "__main__":
    successful_arrangements = 0
    max_attempts = 1000

    while successful_arrangements < 4:
        queens = generate_random_queens()
        if successful_arrangements == 0:
            print("Случайные успешные расстановки:")

        print_chessboard(queens)
        print()

        successful_arrangements += 1