from pathlib import Path

INPUT_FILENAME="input"

TAGS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
} 

def part1(input_lines: list[str]):
    tag_values = { ")": 3, "]": 57, "}": 1197, ">": 25137 }

    broken_tags = []
    for line in input_lines:
        awaiting = []
        for c in line: 
            if c in TAGS.keys():
                awaiting.append(TAGS[c])

            if c in TAGS.values():
                if c != awaiting.pop():
                    broken_tags.append(c)

    points = sum([tag_values[c] for c in broken_tags])
    print(points)


def part2(input_lines: list[str]):
    closing_tags = []
    for line in input_lines:
        broken = False
        awaiting = []
        for c in line: 
            if c in TAGS.keys():
                awaiting.append(TAGS[c])

            if c in TAGS.values():
                if c != awaiting.pop():
                    broken = True

        if not broken:
            awaiting.reverse()
            closing_tags.append(awaiting)

    tag_values = { ")": 1, "]": 2, "}": 3, ">": 4 }
    def get_points(tags: list[str]) -> int: 
        points = 0
        for tag in tags:
            points = points * 5 + tag_values[tag]
            
        return points
        
    total_points = [get_points(tags) for tags in closing_tags]
    total_points.sort()
    median = total_points[round(len(total_points) / 2)]
    print(median)


if __name__ == "__main__":
    input_file = Path(__file__).parent / INPUT_FILENAME
    input_lines = input_file.read_text().strip().split("\n")

    part1(input_lines)
    part2(input_lines)