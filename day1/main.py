import pathlib
import sys

INPUT_FILE="input"

def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]

def part1(numbers):
    count = 0
    for i in range(0, len(numbers) - 1):
        if numbers[i + 1] - numbers[i] > 0: 
            count = count + 1

    return count

def part2(numbers):
    window_size = 3

    sums = []
    for i in range(0, len(numbers) - window_size + 1):
        sums.append(sum(numbers[i:i+window_size]))

    return part1(sums)

if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text().strip()
    numbers = parse(puzzle_input)

    print(part1(numbers))
    print(part2(numbers))