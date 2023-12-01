from sys import argv


def get_digits(line: str) -> list[int]:
    digit_lookup = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    # list[(index, numeric value)]
    result: set[tuple[int, int]] = set()

    def first_last_occurance(name: str, value: int) -> None:
        first, last = line.find(name), line.rfind(name)
        if first != -1:
            result.add((first, value))
        if last != -1:
            result.add((last, value))

    for (name, value) in digit_lookup.items():
        first_last_occurance(name, value)
        first_last_occurance(str(value), value)

    print(line)
    print(result)
    return [x[1] for x in sorted(list(result), key=lambda x: x[0])]


def main(args: list[str]):
    result = 0

    file = open(args[0])
    for line in file.readlines():
        line = line.strip()
        digits = get_digits(line)
        first, last = digits[0], digits[-1]
        result += first * 10 + last

    print(f"Sum of all calibration values is: {result}")


if __name__ == "__main__":
    args = argv[1:]
    if len(args) == 0:
        print("Expected at least 1 command line argument.")
    else:
        main(args)
