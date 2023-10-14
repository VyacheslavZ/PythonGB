# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
# Задача 2, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Только здесь не только 16  представление


import argparse
import logging


FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO, filename='func.log', encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def get_number(number: int, mod: int = 10) -> str:
    """
    Функция получает целое число, систему исчисления и возвращает его  строковое представление.
    :param number: само число
    :param mod: система исчисления
    :return: строковое представление
    """
    result = ''
    if mod < 0:
        logger.error(f'Система исчисления {mod} не существует')
        return 'error'
    while number != 0:
        try:
            result = str(number % mod) + result
            number //= mod
        except ZeroDivisionError as e:
            logger.error(f'Система исчисления {mod} не существует')
            return 'error'
    logger.info(f'{number}, {mod} = {result}')
    return result


def parser_func():
    parser = argparse.ArgumentParser(description='Получаем аргументы из строки')
    parser.add_argument('--number')
    parser.add_argument('--mod', default=2)
    args = parser.parse_args()
    print(args)
    return get_number(int(args.number), int(args.mod))


if __name__ == '__main__':
    print(get_number(100, -6))
    print(get_number(100, 4))
    print(get_number(100, 0))

    # Реализация из командной строки
    # print(parser_func())
    # Пример написания в командной строке:   python Python\hw_15\1.py --number 500 --mod 2