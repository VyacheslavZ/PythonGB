from list_averager import ListAverager

first_list = [2, 5, 25, 8, 3, 13, 9, 23, 4, 1]  # среднее значение 9.3
second_list = [78, 3, 8, 22, 6, 9, 15, 88, 1, 10]  # среднее значение 24


def test_first_list():
    la = ListAverager(first_list, second_list)
    assert sorted(first_list) == sorted(la.first_list)


def test_second_list():
    la = ListAverager(first_list, second_list)
    assert sorted(second_list) == sorted(la.second_list)


def test_average_first_list():
    la = ListAverager(first_list, second_list)
    assert la.average_first_list == 9.3


def test_average_second_list():
    la = ListAverager(first_list, second_list)
    assert la.average_second_list == 24