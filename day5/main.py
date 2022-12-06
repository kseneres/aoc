from collections import namedtuple
import pathlib
from typing import Dict, List

INPUT_FILE = "example"
INPUT_FILE = "input"

Instruction = namedtuple("Instruction", ["count", "start", "end"])


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]


def part1(stacks: Dict[str, List[str]], instructions: List[Instruction]):
    for instruction in instructions:
        count, start, end = instruction

        for _ in range(count):
            crate = stacks[start].pop()
            stacks[end].append(crate)

    crate_tops = [v[-1] for _, v in sorted(stacks.items())]
    return "".join(crate_tops)


def part2(stacks: Dict[str, List[str]], instructions: List[Instruction]):
    for instruction in instructions:
        count, start, end = instruction

        crates = stacks[start][-count:]
        del stacks[start][-count:]

        stacks[end] += crates

    crate_tops = [v[-1] for _, v in sorted(stacks.items())]
    return "".join(crate_tops)


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text()

    instructions: List[Instruction] = []
    stacks: Dict[str, List[str]] = {}

    for line in puzzle_input.split("\n"):
        if line.startswith("move"):
            steps = line.split(" ")
            count, start, end = int(steps[1]), int(steps[3]), int(steps[5])
            instructions.append((count, start, end))
        else:
            columns = list(line)
            for i in range(0, len(columns), 4):
                c = columns[i + 1]
                index = int(i / 4) + 1
                if c.isalpha():
                    if index in stacks:
                        stacks[index].insert(0, c)
                    else:
                        stacks[index] = [c]

    print(part1({**stacks}, instructions))
    print(part2({**stacks}, instructions))