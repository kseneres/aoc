import pathlib
from dataclasses import dataclass
from typing import List, NamedTuple, Tuple

INPUT_FILE="input"

class Point(NamedTuple):
    x: int
    y: int

class Line(NamedTuple):
    start: Point
    end: Point

    def get_magnitude(self) -> int: 
        return max(abs(self.start.x - self.end.x), abs(self.start.y - self.end.y))

@dataclass
class Board:
    board: List[List[int]]

    def __init__(self, x: int, y: int) -> None:
        self.board = [[0] * (x + 1) for _ in range(y + 1)]

    def process_line(self, line: Line, include_diagonal = False):
        top_point = line.start if line.start.y < line.end.y else line.end
        left_point = line.start if line.start.x < line.end.x else line.end
        magnitude = line.get_magnitude()

        if include_diagonal and line.start.x != line.end.x and line.start.y != line.end.y: 
            slope = int((line.end.y - line.start.y) / (line.end.x - line.start.x))
            for i in range(magnitude + 1): 
                self.board[left_point.y + (slope * i)][left_point.x + i] += 1
        else:
            for i in range(magnitude + 1): 
                if line.start.x == line.end.x:
                    self.board[top_point.y + i][top_point.x] += 1
                if line.start.y == line.end.y:
                    self.board[left_point.y][left_point.x + i] += 1
                

    def get_overlap_count(self) -> int:
        count = 0
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                p = self.board[y][x]

                if p > 1:
                    count += 1

        return count

    def __str__(self) -> str:
        return "\n".join(["".join([str(c) if c > 0 else "." for c in row]) for row in self.board])


def process_input(input_lines: List[str]) -> List[Line]: 

    def parse_line(line: str) -> Line:
        points = [p.split(",") for p in line.split(" -> ")]
        p1, p2 = [Point(int(x), int(y)) for x, y in points]
        
        return Line(p1, p2)
    
    lines = [parse_line(line) for line in input_lines]
    return lines

def get_dimensions(lines: List[Line]) -> Tuple[int, int]: 
    max_x = max_y = 0
    for line in lines:
        max_x = max(max_x, line.start.x, line.end.x)
        max_y = max(max_y, line.start.y, line.end.y)

    return max_x, max_y


def part1(lines: List[Line]):
    max_x, max_y = get_dimensions(lines)
    board = Board(max_x, max_y)

    for line in lines:
        board.process_line(line)

    print(board)

    count = board.get_overlap_count()
    print(f"overlap count: {count}")

    return

def part2(lines: List[Line]):
    max_x, max_y = get_dimensions(lines)
    board = Board(max_x, max_y)
    
    for line in lines:
        board.process_line(line, include_diagonal=True)

    print(board)

    count = board.get_overlap_count()
    print(f"overlap count: {count}")

    return


if __name__ == "__main__":
    input_lines = pathlib.Path(INPUT_FILE).read_text().strip().split("\n")
    lines = process_input(input_lines)

    part1(lines)
    part2(lines)