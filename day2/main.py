import pathlib
import sys

INPUT_FILE="input"

def parse(puzzle_input):
    return [line.split() for line in puzzle_input.split("\n")]

def part1(data):
    position = 0
    depth = 0
    for direction, value in data:
        value = int(value)
        if direction == "forward":
            position += value
        elif direction == "down":
            depth += value
        elif direction == "up":
            depth -= value

    print(position * depth)

def part2(data):
    aim = 0
    position = 0
    depth = 0
    for direction, value in data:
        value = int(value)
        if direction == "forward":
            position += value
            depth += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value

    print(position * depth)

if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text().strip()
    data = parse(puzzle_input)

    part1(data)
    part2(data)