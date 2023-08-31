# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

my_list = [4, 5 ,456 ,4654, 54, 54, 87, 897, 897, 654 ,897, 897]
new_list = []
my_set = set(my_list)

for item in my_set:
    if my_list.count(item) > 1:
        new_list.append(item)

print(new_list)