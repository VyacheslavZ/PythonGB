# Доработать задачи 5-6 семинара 10. Создать класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и
# параметры для этого типа.
# Внутри класса создать экземпляр на основе переданного типа и вернуть его
# из класса-фабрики.

from animal import Fish, Bird, Cat, Animal


class Factory:
    _params = {}

    @classmethod
    def build_animal(cls, animal_type, name, color, size,
                     max_depth=None, habitat=None, hairy=None) -> Animal:
        cls._params = dict(name=name, color=color, size=size,
                           max_depth=max_depth, habitat=habitat, hairy=hairy)
        return cls._choice_animal(animal_type)

    @classmethod
    def _choice_animal(cls, animal_type):
        match animal_type:
            case 'Fish':
                return cls._create_fish(**cls._params)
            case 'Bird':
                return cls._create_bird(**cls._params)
            case 'Cat':
                return cls._create_cat(**cls._params)
            case _:
                return Animal('Jerry', 'grey', 8.5)

    @classmethod
    def _create_fish(cls, name, color, size, max_depth, **_) -> Fish:
        return Fish(name=name, color=color, size=size, max_depth=max_depth)

    @classmethod
    def _create_bird(cls, name, color, size, habitat, **_) -> Bird:
        return Bird(name=name, color=color, size=size, habitat=habitat)

    @classmethod
    def _create_cat(cls, name, color, size, hairy, **_) -> Cat:
        return Cat(name=name, color=color, size=size, hairy=hairy)


def main():
    fish = Factory.build_animal('Fish', 'Flounder', 'orange', 10.2, 15.0)
    bird = Factory.build_animal('Bird', 'Chichi', 'white', 82.3, 'forest')
    cat = Factory.build_animal('Cat', 'Tom', 'black and white', 11, True)
    unknown = Factory.build_animal('Non-type', 'noname', 'blue',
                                   12_560, 15.0, 'forest', True)

    animals = (fish, bird, cat, unknown)
    for animal in animals:
        print(animal.get_info())


if __name__ == '__main__':
    main()