from pathlib import Path
from typing import NamedTuple

INPUT_FILENAME="input"

class Fold(NamedTuple):
    axis: int
    value: int

def display_grid(grid: list[list[int]]):
    for row in grid:
        print("".join(["." if v == 0 else "#" for v in row]))

def fold_grid(grid: list[list[int]], fold: Fold) -> list[list[int]]:
    if fold.axis == "y":
        for y in range(fold.value + 1, len(grid)):
            new_y = fold.value - (y - fold.value)
            for x in range(len(grid[y])):
                grid[new_y][x] += grid[y][x]

        return grid[:fold.value]

    if fold.axis == "x":
        for y in range(len(grid)):
            for x in range(fold.value + 1, len(grid[y])):
                new_x = fold.value - (x - fold.value)
                grid[y][new_x] += grid[y][x]

        return [row[:fold.value] for row in grid]

def part1(grid: list[list[int]], fold: Fold):
    grid = fold_grid(grid, fold)
    dot_count = sum([len([True for v in row if v > 0]) for row in grid])
    print(dot_count) 

def part2(grid: list[list[int]], folds: list[Fold]):
    for fold in folds:
        grid = fold_grid(grid, fold)

    display_grid(grid)

if __name__ == "__main__":
    input_file = Path(__file__).parent / INPUT_FILENAME
    input_lines = input_file.read_text().strip().split("\n")

    dots = [line.split(",") for line in input_lines if not line.startswith("fold") and len(line) > 0]
    dots = [(int(x), int(y)) for x, y in dots]

    fold_instructions = [line.strip("fold along ") for line in input_lines if line.startswith("fold")]
    folds: list[Fold] = []
    for instruction in fold_instructions:
        axis, value = instruction.split("=")
        folds.append(Fold(axis, int(value)))

    # calculate initial grid size based on first fold instructions
    initial_x_size = next(i for i in folds if i.axis == "x").value * 2 + 1
    initial_y_size = next(i for i in folds if i.axis == "y").value * 2 + 1

    # create and populate grid with dots
    grid = [[0] * initial_x_size for _ in range(initial_y_size)]
    for x, y in dots:
        grid[y][x] = 1

    part1(grid, folds[0])
    part2(grid, folds)