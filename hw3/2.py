# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

from typing import Dict, Any

WORK_TEXT = """
            The Olympic Games have their own flag and motto. The flag is white with five circles. The circles represent the five 
            continents of Africa, Asia, Australia, Europe and North and South America. The circles are black, blue, green, red and yellow. 
            The flag of every country in the games has at least one of these colours. The motto of the Olympics is 'Faster, higher, stronger'. 
            The most exciting moment of the opening ceremony is the lighting of the Olympic Flame, another symbol of the Olympic Games. 
            Runners bring a torch from the valley of Olympia in Greece. Thousands of runners take part in the journey. 
            The journey starts four weeks before the opening of the Games. At the opening ceremony, the final runner carries the torch to 
            the stadium, and lights the new Olympic games Flame. Then there is a very big song, dance and music show. The Olympic Flame burns 
            until the end of the Games. The International Olympic Committee works hard between the Games. They choose the place for the next 
            Olympics and new sports for them too.
            """
            
FREQUENT_COUNT = 10

def most_frequent_words(text: str, count_words: int) -> dict:
    words_list = text.upper() \
        .replace(".", " ") \
        .replace(",", " ") \
        .replace(";", " ") \
        .replace(":", " ") \
        .replace("!", " ") \
        .replace("?", " ") \
        .replace(" - ", " ") \
        .split()
    words_count = {}
    for w in words_list:
        words_count[w] = words_list.count(w)
    return dict(sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:count_words])


def main():
    for i, w in enumerate(most_frequent_words(WORK_TEXT, FREQUENT_COUNT).items(), 1):
        print(f"{i:2}. {w[0]:<10} - {w[1]}")


if __name__ == "__main__":
    main()