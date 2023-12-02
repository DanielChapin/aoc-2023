from sys import argv


class Round:
    color_count: dict[str, int]

    def __init__(self) -> None:
        self.color_count = dict()

    def is_possible(self, color_max: dict[str, int]) -> bool:
        for color, count in self.color_count.items():
            max_count = color_max.get(color, 0)
            if count > max_count:
                return False
        return True

    def update_min_colors(self, min_colors: dict[str, int]):
        for color, count in self.color_count.items():
            color_min = min_colors.get(color, 0)
            if count > color_min:
                min_colors[color] = count

    @staticmethod
    def from_str(line: str) -> 'Round':
        entries = map(lambda entry: entry.split(), line.strip().split(','))
        result = Round()
        for entry in entries:
            result.color_count[entry[1]] = int(entry[0])
        return result

    def __str__(self) -> str:
        return ", ".join(
            map(lambda item: f"{item[1]} {item[0]}", self.color_count.items()))


class Game:
    game_id: int
    rounds: list[Round]

    def __init__(self, game_id: int, rounds: list[Round] = []) -> None:
        self.game_id = game_id
        self.rounds = rounds

    def is_possible(self, color_max: dict[str, int]) -> bool:
        return all(map(lambda round_instance: round_instance.is_possible(color_max), self.rounds))

    def min_colors(self) -> dict[str, int]:
        result: dict[str, int] = dict()
        for round_instance in self.rounds:
            round_instance.update_min_colors(result)
        return result

    def cube_power(self) -> int:
        result = 1
        for count in self.min_colors().values():
            result *= count
        return result

    @staticmethod
    def from_str(line: str) -> 'Game':
        entries = line.strip().split(':')
        game_id = int(entries[0].removeprefix('Game '))
        rounds = list(map(Round.from_str, entries[1].split(';')))
        return Game(game_id, rounds)

    def __str__(self) -> str:
        return f"Game {self.game_id}: {'; '.join(map(str, self.rounds))}"


def solution(args: list[str]):
    file = open(args[0], 'r')
    games = map(Game.from_str, file.readlines())

    print(sum(map(Game.cube_power, games)))


def main():
    args = argv[1:]
    if len(args) == 0:
        print("Expected at least 1 command line argument.")
        return

    solution(args)


if __name__ == "__main__":
    main()
