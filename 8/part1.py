from sys import argv
import re


class Network:
    instructions: list[int]
    edges: dict[str, list[str]]

    def steps_between(self, start: str = "AAA", goal: str = "ZZZ") -> int:
        current: str = start
        step = 0

        while current != goal:
            instruction = self.instructions[step % len(self.instructions)]
            current = self.edges[current][instruction]
            step += 1

        return step

    @staticmethod
    def from_file(filepath: str) -> 'Network':
        with open(filepath, "r") as f:
            lines = list(filter(lambda line: line != "",
                         map(str.strip, f.readlines())))
            network = Network()

            # Instructions
            instruction_lookup = {
                'R': 1,
                'L': 0,
            }
            network.instructions = list(
                map(lambda char: instruction_lookup[char], lines[0].upper()))

            # Edges
            network.edges = dict()
            for line in lines[1:]:
                parsed = re.match(
                    r"^\s*(?P<node>\w+)\s*=\s*\((?P<neighbors>[\w,\s]+)\)\s*$", line)
                network.edges[parsed.group("node")] = list(
                    map(str.strip, parsed.group("neighbors").split(',')))

            return network


def solution(args: list[str]):
    network = Network.from_file(args[0])
    print(network.steps_between())


def main():
    args = argv[1:]
    if len(args) == 0:
        print("Expected at least 1 command line argument.")
        return

    solution(args)


if __name__ == "__main__":
    main()
