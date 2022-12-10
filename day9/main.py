from collections import namedtuple
from dataclasses import dataclass, field, replace
import dataclasses
import pathlib
from typing import Dict, List, Tuple

INPUT_FILE = "example"
INPUT_FILE = "input"


Motion = namedtuple("Motion", ["direction", "steps"])
Point = namedtuple("Point", ["x", "y"])


def parse(puzzle_input: str) -> List[Motion]:
    lines = [line for line in puzzle_input.split("\n")]
    motions = []
    for line in lines:
        direction, step = line.split(" ")
        motions.append(Motion(direction, int(step)))

    return motions


@dataclass
class Node:
    id: str
    tail: "Node" = None
    positions: List[Point] = field(default_factory=lambda: [Point(0, 0)])

    def move(self, new_point: Point):
        # first add new position to self
        node = self
        node.positions.append(new_point)

        # adjust tails
        while node and node.tail:
            head_point = node.positions[-1]
            tail_point = node.tail.positions[-1]

            x_delta = head_point.x - tail_point.x
            y_delta = head_point.y - tail_point.y
            stretched = abs(x_delta) > 1 or abs(y_delta) > 1

            if stretched:
                x, y = tail_point
                if x_delta != 0:
                    x = tail_point.x + (1 if x_delta > 0 else -1)

                if y_delta != 0:
                    y = tail_point.y + (1 if y_delta > 0 else -1)

                new_point = Point(x, y)
                node.tail.positions.append(new_point)

            # go to next tail
            node = node.tail


def move_knots(motions: List[Motion], knots: 2):
    head = Node("H")

    knot = head
    for id in range(1, knots):
        knot.tail = Node(id)
        knot = knot.tail

    for direction, steps in motions:
        for _ in range(steps):
            x, y = head.positions[-1]
            if direction == "U":
                y += 1
            if direction == "D":
                y -= 1
            if direction == "R":
                x += 1
            if direction == "L":
                x -= 1

            new_point = Point(x, y)
            head.move(new_point)

    knot = head
    while knot:
        p = set(knot.positions)
        print(knot.id, len(p))

        if knot.tail == None:
            return len(p)

        knot = knot.tail


def part1(motions: List[Motion]):
    return move_knots(motions, 2)


def part2(motions: List[Motion]):
    return move_knots(motions, 10)


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text()
    motions = parse(puzzle_input)

    print(part1(motions))
    print(part2(motions))
