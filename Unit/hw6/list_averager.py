from statistics import mean
from typing import List


class ListAverager:
    def __init__(self, first_list: List, second_list: List) -> None:
        self.__first_list: List = first_list
        self.__second_list: List = second_list
        self.__average_first_list: float = None
        self.__average_second_list: float = None

    @property
    def first_list(self) -> List:
        return self.__first_list

    @property
    def second_list(self) -> List:
        return self.__second_list

    @property
    def average_first_list(self) -> float:
        if self.__average_first_list is None:
            self.__average_first_list = mean(self.__first_list)
        return self.__average_first_list

    @property
    def average_second_list(self) -> float:
        if self.__average_second_list is None:
            self.__average_second_list = mean(self.__second_list)
        return self.__average_second_list