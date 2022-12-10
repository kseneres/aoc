from collections import namedtuple
from dataclasses import dataclass, field, replace
import dataclasses
import pathlib
from typing import Dict, List, Tuple

INPUT_FILE = "example"
INPUT_FILE = "input"


def parse(puzzle_input: str) -> List[str]:
    return [line for line in puzzle_input.split("\n")]


def part1(instructions: List[str]):
    cycle = 1
    register = 1

    cycles: Dict[int, int] = {}
    for instruction in instructions:
        if instruction.startswith("noop"):
            cycle += 1
        else:
            _, value = instruction.split(" ")
            cycle += 1

            if cycle == 20 or (cycle + 20) % 40 == 0:
                cycles[cycle] = register

            cycle += 1
            register += int(value)

        if cycle == 20 or (cycle + 20) % 40 == 0:
            cycles[cycle] = register

    total = 0
    for k, v in cycles.items():
        total += k * v

    return total


def part2(instructions: List[str]):
    register = 1
    buffer: List[List[str]] = []

    second = False
    for clock in range(240):
        if clock % 40 == 0:
            buffer.append([])

        h = clock % 40
        sprite = register >= h - 1 and register <= h + 1
        buffer[-1].append("#" if sprite else ".")

        instruction = instructions[0]
        if instruction.startswith("noop"):
            instructions.pop(0)
        else:
            _, value = instruction.split(" ")
            if second:
                instructions.pop(0)
                register += int(value)

            second = not second

    lines = ["".join(line) for line in buffer]
    return "\n".join(lines)


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text()
    instructions = parse(puzzle_input)

    print(part1(instructions))
    print(part2(instructions))
