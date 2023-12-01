from sys import argv
import re


def main(args: list[str]):
    result = 0

    file = open(args[0])
    for line in file.readlines():
        line = line.strip()
        digits = [int(char) for char in re.findall('\d', line)]
        first, last = digits[0], digits[-1]
        result += first * 10 + last

    print(f"Sum of all calibration values is: {result}")


if __name__ == "__main__":
    args = argv[1:]
    if len(args) == 0:
        print("Expected at least 1 command line argument.")
    else:
        main(args)
