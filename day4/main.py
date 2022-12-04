import pathlib

INPUT_FILE = "example"
INPUT_FILE = "input"


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split()]


def part1(assignments):
    pairs = map(lambda a: a.split(","), assignments)
    overlap_count = 0
    for f, s in pairs:
        fs, fe = f.split("-")
        ss, se = s.split("-")

        f_set = set([i for i in range(int(fs), int(fe) + 1)])
        s_set = set([i for i in range(int(ss), int(se) + 1)])

        intersection = f_set & s_set
        if len(intersection) == len(f_set) or len(intersection) == len(s_set):
            overlap_count += 1

    return overlap_count


def part2(assignments):
    pairs = map(lambda a: a.split(","), assignments)
    overlap_count = 0
    for f, s in pairs:
        fs, fe = f.split("-")
        ss, se = s.split("-")

        f_set = set([i for i in range(int(fs), int(fe) + 1)])
        s_set = set([i for i in range(int(ss), int(se) + 1)])

        intersection = f_set & s_set
        if len(intersection) > 0:
            overlap_count += 1

    return overlap_count


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text()
    assignments = [round for round in puzzle_input.split()]

    print(part1(assignments))
    print(part2(assignments))