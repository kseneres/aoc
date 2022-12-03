import pathlib
import sys

INPUT_FILE = "example"
INPUT_FILE = "input"


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]


def part1(groups):
    return max([sum(g) for g in groups])


def part2(groups):
    sums = [sum(g) for g in groups]
    sums.sort(reverse=True)
    return sum(sums[0:3])


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text()

    groups = []
    current_group = []
    for line in puzzle_input.split("\n"):
        if not line:
            groups.append(current_group)
            current_group = []
        else:
            current_group.append(int(line))

    print(part1(groups))
    print(part2(groups))
