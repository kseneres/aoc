from enum import Enum
import pathlib

INPUT_FILE = "input"


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]


def part1(rounds):
    score = 0

    for round in rounds:
        o, y = round.split()

        other = ord(o) - ord("A")
        you = ord(y) - ord("X")

        tie = you == other
        win = (you - 1) % 3 == other

        if tie:
            score += 3
        elif win:
            score += 6

        score += ord(y) - ord("X") + 1

    return score


def part2(rounds):
    scores = [1, 2, 3]

    def get_score(round: str):
        o, y = round.split()

        index = ord(o) - ord("A") + 2
        offset = ord(y) - ord("X")

        score = scores[(index + offset) % 3]
        score += (ord(y) - ord("X")) * 3

        return score

    score = sum([get_score(round) for round in rounds])
    return score


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text()
    rounds = [round for round in puzzle_input.split("\n")]

    print(part1(rounds))
    print(part2(rounds))