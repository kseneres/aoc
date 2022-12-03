import pathlib

INPUT_FILE = "example"
INPUT_FILE = "input"


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]


def part1(rounds):
    halves = [(a[: len(a) // 2], a[len(a) // 2 :]) for a in rounds]
    common = [set(f) & set(s) for f, s in halves]

    priority = [ord((c.pop())) for c in common]
    adjusted = [p - 96 if p > 96 else p - 64 + 26 for p in priority]

    score = sum(adjusted)
    return score


def part2(rounds):
    n = 3
    groups = [rounds[i : i + n] for i in range(0, len(rounds), n)]
    common = [set.intersection(*[set(sack) for sack in group]) for group in groups]

    priority = [ord((c.pop())) for c in common]
    adjusted = [p - 96 if p > 96 else p - 64 + 26 for p in priority]

    score = sum(adjusted)
    return score


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text()
    rounds = [round for round in puzzle_input.split()]

    print(part1(rounds))
    print(part2(rounds))