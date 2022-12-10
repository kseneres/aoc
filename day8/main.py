from collections import namedtuple
from dataclasses import dataclass
import pathlib
from typing import Dict, List, Tuple

INPUT_FILE = "example"
INPUT_FILE = "input"


def parse(puzzle_input: str) -> List[List[int]]:
    return [[int(count) for count in list(line)] for line in puzzle_input.split("\n")]


def part1(grid: List[List[int]]):
    visible_count = 0

    for r in range(1, len(grid[0]) - 1):
        for c in range(1, len(grid[r]) - 1):
            tree = grid[r][c]

            top = [grid[r - i][c] for i in range(1, r + 1)]
            bottom = [grid[r + i][c] for i in range(1, len(grid[r]) - r)]
            left = grid[r][0:c]
            right = grid[r][c + 1 :]

            if max(top) < tree or max(bottom) < tree or max(left) < tree or max(right) < tree:
                visible_count += 1

    edges = (len(grid) * 2) + ((len(grid[0]) - 2) * 2)
    return edges + visible_count


def part2(grid: List[List[int]]):
    max_scenic_score = 0
    for r in range(1, len(grid[0]) - 1):
        for c in range(1, len(grid[r]) - 1):
            tree = grid[r][c]

            top = [grid[r - i][c] for i in range(1, r + 1)]
            bottom = [grid[r + i][c] for i in range(1, len(grid[r]) - r)]
            left = grid[r][0:c]
            right = grid[r][c + 1 :]

            t = [int(i) + 1 for i, e in enumerate(top) if e >= tree]
            t = t[0] if len(t) > 0 else len(top)

            b = [int(i) + 1 for i, e in enumerate(bottom) if e >= tree]
            b = b[0] if len(b) > 0 else len(bottom)

            left.reverse()
            l = [int(i) + 1 for i, e in enumerate(left) if e >= tree]
            l = l[0] if len(l) > 0 else len(left)

            ri = [int(i) + 1 for i, e in enumerate(right) if e >= tree]
            ri = ri[0] if len(ri) > 0 else len(right)

            score = t * b * l * ri
            if score > max_scenic_score:
                max_scenic_score = score

            # if max(top) < tree or max(bottom) < tree or max(left) < tree or max(right) < tree:
            #     max_scenic_score += 1

    return max_scenic_score


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text()
    grid = parse(puzzle_input)

    print(part1(grid))
    print(part2(grid))