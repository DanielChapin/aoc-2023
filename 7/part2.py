from sys import argv
from enum import Enum, auto
import re


class CamelCard:
    valid_cards = ['J'] + list(map(str, range(2, 10))) + ['T', 'Q', 'K', 'A']
    value_lookup = dict(zip(valid_cards, range(len(valid_cards))))

    @staticmethod
    def value(symbol: str) -> int:
        return CamelCard.value_lookup[symbol]


class CamelHandType(Enum):
    """
    Hand types ordered by value increasing (note apparently auto doesn't work the same on all python versions.)
    """
    HIGH = 0, [1, 1, 1, 1, 1]
    PAIR = 1, [2, 1, 1, 1]
    TWO_PAIR = 2, [2, 2, 1]
    THREE_OF_A_KIND = 3, [3, 1, 1]
    FULL_HOUSE = 4, [3, 2]
    FOUR_OF_A_KIND = 5, [4, 1]
    FIVE_OF_A_KIND = 6, [5]

    def rank(self) -> int:
        return self.value[0]

    def card_counts(self) -> list[int]:
        return self.value[1]

    @staticmethod
    def from_card_counts(counts: list[int]) -> 'CamelHandType':
        for hand_type in CamelHandType._member_map_.values():
            if hand_type.card_counts() == counts:
                return hand_type
        return None


class CamelHand:
    cards: str
    bid: int

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid

    def card_values(self) -> tuple[int]:
        return tuple(CamelCard.value(card) for card in self.cards)

    def hand_type(self) -> CamelHandType:
        count_lookup = dict(((x, self.cards.count(x)) for x in set(self.cards)))

        if 'J' not in count_lookup or len(count_lookup.items()) <= 1:
            counts = sorted(list(count_lookup.values()), reverse=True)
            return CamelHandType.from_card_counts(counts)

        max_card = max(filter(lambda x: x[0] != 'J', count_lookup.items()), key=lambda x: x[1])[0]

        count_lookup[max_card] += count_lookup['J']
        count_lookup.pop('J')
        counts = sorted(list(count_lookup.values()), reverse=True)
        return CamelHandType.from_card_counts(counts)

    @staticmethod
    def from_str(value: str) -> 'CamelHand':
        parsed: re.Match[str] = re.match(
            r"^(?P<cards>[2-9TJQAK]{5})\s+(?P<bid>\d+)$", value)
        return CamelHand(parsed.group("cards"), int(parsed.group("bid")))

    def __str__(self) -> str:
        return f"{self.cards} {self.bid}"


def solution(args: list[str]):
    with open(args[0]) as f:
        hands = list(map(CamelHand.from_str, f.readlines()))
        hands.sort(key=lambda hand: (
            hand.hand_type().rank(), hand.card_values()))
        total = sum(map(lambda ix: (ix[0] + 1) * ix[1].bid, enumerate(hands)))
        print(total)


def main():
    args = argv[1:]
    if len(args) == 0:
        print("Expected at least 1 command line argument.")
        return

    solution(args)


if __name__ == "__main__":
    main()
