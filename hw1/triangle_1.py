#Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
#Дано a, b, c — стороны предполагаемого треугольника. 
#Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
#Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


a = int (input("Введите сторону a: "))
b = int (input("Введите сторону b: "))
c = int (input("Введите сторону c: "))

if a < b + c and b < a + c and c < a + b:
    print('Треугольник существует')
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or b == c or a == c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольник не существует')