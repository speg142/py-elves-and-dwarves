from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass


class Elf(Player, ABC):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self.__musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a "
              f"song on the {self.__musical_instrument}")


class Dwarf(Player, ABC):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self.__favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.__favourite_dish}")


class ElfRanger(Elf, ABC):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self.__bow_level = bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. "
                f"{self.nickname} has bow of the {self.__bow_level} level")

    def get_rating(self) -> int:
        return self.__bow_level * 3


class Druid(Elf, ABC):
    def __init__(self,
                 nickname: str,
                 musical_instrument:
                 str, favourite_spell: str) -> None:
        super().__init__(nickname, musical_instrument)
        self.__favourite_spell = favourite_spell

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. "
                f"{self.nickname} has a "
                f"favourite spell: {self.__favourite_spell}")

    def get_rating(self) -> int:
        return len(self.__favourite_spell)


class DwarfWarrior(Dwarf, ABC):
    def __init__(self,
                 nickname: str,
                 favourite_dish:
                 str, hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self.__hummer_level = hummer_level

    def player_info(self) -> str:
        return (f"Dwarf warrior {self.nickname}. "
                f"{self.nickname} has a "
                f"hummer of the {self.__hummer_level} level")

    def get_rating(self) -> int:
        return self.__hummer_level + 4


class DwarfBlacksmith(Dwarf, ABC):
    def __init__(self,
                 nickname: str,
                 favourite_dish: str,
                 skill_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self.__skill_level = skill_level

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname} "
                f"with skill of the {self.__skill_level} level")

    def get_rating(self) -> int:
        return self.__skill_level


def calculate_team_total_rating(player: list[Player]) -> str:
    return sum(player.get_rating() for player in player)


def elves_concert(player: list[Elf]) -> str:
    return (player.play_elf_song for player in player)


def feast_of_the_dwarves(player: list[Dwarf]) -> str:
    return (player.eat_favourite_dish for player in player)
