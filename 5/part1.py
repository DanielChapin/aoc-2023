from sys import argv
from itertools import groupby
import re
from re import Match


class RangeMapping:
    src_start: int
    dst_start: int
    range_len: int

    IDENTITY: 'RangeMapping' = None

    def __init__(self, src: int, dst: int, size: int) -> None:
        self.src_start = src
        self.dst_start = dst
        self.range_len = size

    def contains_value(self, src_value: int) -> bool:
        return self.src_start <= src_value and src_value < self.src_start + self.range_len

    def convert(self, src_value: int) -> int:
        return src_value + self.dst_start - self.src_start

    @staticmethod
    def from_str(text: str) -> 'RangeMapping':
        result = RangeMapping(0, 0, 0)

        regex_match = re.match('^(\d+)\s+(\d+)\s+(\d+)\s*$', text)
        dst, src, size = regex_match.groups()
        result.src_start = int(src)
        result.dst_start = int(dst)
        result.range_len = int(size)

        return result


RangeMapping.IDENTITY = RangeMapping(0, 0, 0)


class Map:
    ranges: list[RangeMapping]
    src_name: str
    dst_name: str

    def __init__(self) -> None:
        self.ranges = []

    def get_range_for(self, src_value: int) -> RangeMapping:
        for range_map in self.ranges:
            if range_map.contains_value(src_value):
                return range_map
        return RangeMapping.IDENTITY

    def convert(self, src_value: int) -> int:
        range_map = self.get_range_for(src_value)
        return range_map.convert(src_value)

    def to_location(self, src_value: int, map_lookup: dict[str, 'Map']) -> int:
        conversion = self.convert(src_value)
        if self.dst_name == 'location':
            return conversion

        return map_lookup[self.dst_name].to_location(conversion, map_lookup)

    @staticmethod
    def from_str(text: str) -> 'Map':
        result = Map()
        regex_match: Match[str] = re.match(
            '^(\w+)-to-(\w+)\s+map:\n\s*([\d\s\n]+)\s*$', text.strip())

        src_name, dst_name, data = regex_match.groups()

        result.src_name = src_name
        result.dst_name = dst_name
        result.ranges = list(map(RangeMapping.from_str, data.split('\n')))

        return result


def solution(args: list[str]):
    file = open(args[0])

    # Parsing seed ids
    search = re.match("^seeds:\s*([\d\s]+)\s*$", file.readline())
    seed_ids = list(map(int, search.group(1).split()))

    # Consuming extra \n
    file.readline()

    # Parsing maps
    map_sources = map(
        lambda group: ''.join(group[1]),
        filter(
            lambda group: not group[0],
            groupby(file.readlines(), lambda x: x == '\n')
        )
    )
    maps = list(map(Map.from_str, map_sources))
    map_lookup: dict[str, Map] = dict(
        map(lambda map_instance: (map_instance.src_name, map_instance), maps))
    start_map = map_lookup['seed']

    locations = list(map(lambda seed_id: start_map.to_location(
        seed_id, map_lookup), seed_ids))
    print(min(locations))


def main():
    args = argv[1:]
    if len(args) == 0:
        print("Expected at least 1 command line argument.")
        return

    solution(args)


if __name__ == "__main__":
    main()
