from collections import namedtuple
from dataclasses import dataclass, field, replace
import dataclasses
import pathlib
import time
from typing import Dict, List, Set, Tuple

INPUT_FILE = "example"
INPUT_FILE = "input"


@dataclass
class Point:
    x: int
    y: int


def parse(puzzle_input: str) -> List[List[int]]:
    lines = [line for line in puzzle_input.split("\n")]
    return [[ord(c) for c in list(line)] for line in lines]


def find_paths(graph, start: Point, end: Point, path=[]):
    path: List[Point] = path + [start]

    current_elevation = graph[start.y][start.x]
    max_elevation = current_elevation + 1

    if start == end:
        print("found it")
        return [path]

    paths: List[List[Point]] = []

    left = None if (start.x - 1) < 0 else Point(start.x - 1, start.y)
    right = None if (start.x + 1) >= len(graph[start.y]) else Point(start.x + 1, start.y)
    up = None if (start.y - 1) < 0 else Point(start.x, start.y - 1)
    down = None if (start.y + 1) >= len(graph) else Point(start.x, start.y + 1)

    options = [left, right, up, down]

    for node in [node for node in options if node]:
        # print(node, graph[node.y][node.x], max_elevation, graph[node.y][node.x] <= max_elevation)
        if node not in path and (graph[node.y][node.x] <= max_elevation):
            new_paths = find_paths(graph, node, end, path)
            # print("paths", start, new_paths)
            for p in new_paths:
                paths.append(p)

    return paths


def part1(grid: List[List[int]]):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ord("S"):
                start = Point(col, row)
            if grid[row][col] == ord("E"):
                end = Point(col, row)

    print(start, end)
    grid[start.y][start.x] = ord("a")
    grid[end.y][end.x] = ord("z") + 1

    paths = find_paths(grid, start, end)
    # print(paths)
    for p in paths:
        if p[-1] == end:
            print("length", len(p))

    shortest = min([len(p) for p in paths if p[-1] == end])
    print(shortest)


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text()
    grid = parse(puzzle_input)

    print(part1(grid))
