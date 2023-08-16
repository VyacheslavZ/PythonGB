# Напишите программу, которая принимает 
# две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def perform_operations(fraction1, fraction2):
    frac1 = Fraction(fraction1)
    frac2 = Fraction(fraction2)

    sum_result = frac1 + frac2
    product_result = frac1 * frac2

    return sum_result, product_result

fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

sum_result, product_result = perform_operations(fraction1, fraction2)

print(f"Сумма дробей: {sum_result}")
print(f"Произведение дробей: {product_result}")