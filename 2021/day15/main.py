from pathlib import Path
from typing import NamedTuple

INPUT_FILENAME="example"

class Point(NamedTuple):
    x: int
    y: int

def part1(risk_levels: list[list[int]]):
    start_position = (0, 0)

    def find_best_path(graph, start: Point, end: Point, path=[]):
        path: list[str] = path + [start]

        if start == end:
            return [path]
        if start.y == len(graph) or start.x == len(graph[start.y]):
            return []
        
        paths = []
        next_x = Point(start.x + 1, start.y)
        next_y = Point(start.x, start.y + 1)

        if next_x.x < len(graph[start.y]):
            new_paths = find_best_path(graph, next_x, end, path)
            paths.extend(new_paths)
            
        if next_y.y < len(graph):
            new_paths = find_best_path(graph, next_y, end, path)
            paths.extend(new_paths)

        return paths

    paths = find_best_path(risk_levels, Point(0, 0), Point(9, 9))
    print(len(paths))

if __name__ == "__main__":
    input_file = Path(__file__).parent / INPUT_FILENAME
    input_lines = input_file.read_text().strip().split("\n")

    risk_levels = [[int(s) for s in line] for line in input_lines]
    for r in risk_levels: print(r)

    part1(risk_levels)