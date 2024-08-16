from sys import argv
import re
import operator as op
from functools import reduce
import math


class Input:
    times: list[int]
    distances: list[int]

    @staticmethod
    def from_file(path: str) -> "Input":
        file_in = "\n".join(open(path).readlines())
        parsed = re.match(
            r"Time:\s*(?P<times>[\d\s]+)\nDistance:\s*(?P<distances>[\d\s]+)", file_in, re.IGNORECASE)

        def ws_int_array(val): return [int(x) for x in val.split()]

        result = Input()
        result.times = ws_int_array(parsed.group("times"))
        result.distances = ws_int_array(parsed.group("distances"))
        return result


def ways_to_beat(time: int, distance: int) -> int:
    d = math.sqrt(time ** 2 - 4 * distance)
    rhs = (time + d) / 2
    lhs = (time - d) / 2
    return max(0, math.ceil(rhs) - math.floor(lhs) - 1)


def solution(args: list[str]):
    params = Input.from_file(args[0])
    print(reduce(op.mul, map(lambda p: ways_to_beat(
        *p), zip(params.times, params.distances)), 1))


def main():
    args = argv[1:]
    if len(args) == 0:
        print("Expected at least 1 command line argument.")
        return

    solution(args)


if __name__ == "__main__":
    main()
