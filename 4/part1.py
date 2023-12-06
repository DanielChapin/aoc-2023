from sys import argv
import re


class Card:
    identifier: int
    winning_nums: set[int]
    numbers: list[int]

    def __init__(self, identifier: int, winning_nums: set[int], numbers: list[int]) -> None:
        self.identifier = identifier
        self.winning_nums = winning_nums
        self.numbers = numbers

    def winners(self) -> list[int]:
        return list(filter(lambda number: number in self.winning_nums, self.numbers))

    def point_value(self):
        count = len(self.winners())
        if count == 0:
            return 0
        return 2 ** (count - 1)

    @staticmethod
    def from_str(text: str) -> 'Card':
        search = re.match('^Card\s+(\d+): ([\d\s]+) \| ([\d\s]+)$', text)
        assert search != None

        identifier = int(search.group(1))
        winning_nums = set(map(int, search.group(2).split()))
        nums = list(map(int, search.group(3).split()))

        return Card(identifier, winning_nums, nums)


def solution(args: list[str]):
    file = open(args[0], 'r')
    cards = list(map(lambda line: Card.from_str(
        line.strip()), file.readlines()))
    total_points = sum(map(Card.point_value, cards))
    print(total_points)


def main():
    args = argv[1:]
    if len(args) == 0:
        print("Expected at least 1 command line argument.")
        return

    solution(args)


if __name__ == "__main__":
    main()
