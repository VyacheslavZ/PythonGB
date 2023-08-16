#Напишите программу, которая получает целое число и возвращает 
# его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

HEX_FACTOR = 16
hex_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']

HEX_FACTOR = 16
hex_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']


def get_number_from_user() -> int:
    enter = input('Введите число: ')
    return int(enter)
original = get_number_from_user


def converter(number: int) -> str:
    res: str = ''
    while number > 0:
        res = str(hex_data[number % HEX_FACTOR]) + res
        number //= HEX_FACTOR
    return res


num = get_number_from_user()
if isinstance(num, int):
    print("Ваше число в 16-чной системе будет: " + converter(num))
else:
    print('Ошибка, проверте корректность ввода!')