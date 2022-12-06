from collections import namedtuple
import pathlib
from typing import Dict, List, Tuple

INPUT_FILE = "example"
INPUT_FILE = "input"


def parse(puzzle_input: str) -> str:
    return puzzle_input


def part1(datastream: str):
    markers = []
    for i, c in enumerate(list(datastream)):
        markers.append(c)
        if len(markers) > 4:
            markers.pop(0)

        if len(set(markers)) == 4:
            return i + 1


def part2(datastream: str):
    WINDOW_SIZE = 14
    for i in range(len(datastream)):
        window = datastream[i : WINDOW_SIZE + i]
        if len(set(window)) == WINDOW_SIZE:
            return i + WINDOW_SIZE


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text()
    datastream = parse(puzzle_input)

    print(part1(datastream))
    print(part2(datastream))