from sys import argv
import re


def should_count(number: str, position: tuple[int, int], symbols: set[tuple[int, int]]) -> bool:
    # .......
    # .nnnnn.
    # .......
    row = position[0]
    for col in range(position[1] - 1, position[1] + len(number) + 1):
        if (row - 1, col) in symbols or (row + 1, col) in symbols:
            return True

    col = position[1]
    return (row, col - 1) in symbols or (row, col + len(number)) in symbols


def solution(args: list[str]):
    file = open(args[0], 'r')

    # Parse input file
    numbers: set[tuple[str, int, int]] = set()
    symbols: set[tuple[int, int]] = set()

    row = 0
    for line in map(str.strip, file.readlines()):
        # Parsing numbers
        for match in re.finditer('\d+', line):
            number = match.group(0)
            col = match.span()[0]
            numbers.add((number, row, col))

        # Parsing symbols
        for match in re.finditer('[^\d\.\n]', line):
            col = match.span()[0]
            symbols.add((row, col))

        row += 1

    # Select the numbers adjacent to a symbol
    result = 0
    for number, row, col in numbers:
        if should_count(number, (row, col), symbols):
            result += int(number)
    print(result)


def main():
    args = argv[1:]
    if len(args) == 0:
        print("Expected at least 1 command line argument.")
        return

    solution(args)


if __name__ == "__main__":
    main()
