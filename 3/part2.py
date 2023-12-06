from sys import argv
import re


def get_gear_ratio(position: tuple[int, int], numbers: list[int], number_lookup: dict[tuple[int, int], int]) -> int:
    adjacent_numbers: set[int] = set()
    row, col = position
    for delta_row in range(-1, 2):
        for delta_col in range(-1, 2):
            target_pos = (row + delta_row, col + delta_col)
            if target_pos in number_lookup:
                adjacent_numbers.add(number_lookup[target_pos])

    if len(adjacent_numbers) != 2:
        return 0

    result = 1
    for index in adjacent_numbers:
        result *= numbers[index]
    return result


def solution(args: list[str]):
    file = open(args[0], 'r')

    # Parse input file
    numbers: list[int] = list()
    number_lookup: dict[tuple[int, int], int] = dict()
    gears: list[tuple[int, int]] = list()

    row = 0
    for line in map(str.strip, file.readlines()):
        # Parsing numbers
        for match in re.finditer('\d+', line):
            number = match.group(0)
            index = len(numbers)
            numbers.append(int(number))

            start = match.span()[0]
            for col in range(start, start + len(number)):
                number_lookup[(row, col)] = index

        # Parsing gears
        for match in re.finditer('\*', line):
            col = match.span()[0]
            gears.append((row, col))

        row += 1

    result = 0
    for position in gears:
        result += get_gear_ratio(position, numbers, number_lookup)
    print(result)


def main():
    args = argv[1:]
    if len(args) == 0:
        print("Expected at least 1 command line argument.")
        return

    solution(args)


if __name__ == "__main__":
    main()
