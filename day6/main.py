from pathlib import Path
from collections import deque

INPUT_FILENAME="input"

def part1(ages: list[int], days: int):
    for day in range(80):
        count = ages.count(0)

        ages = [age - 1 if age > 0 else 6 for age in ages]
        ages = ages + [8] * count

    print(len(ages))

def part2(ages: list[int], days: int):
    CYCLE_TIMER = 7
    CYCLE_OFFSET = 2

    total_fish_count = len(ages)

    # queue for count of fish to spawn, rotated every day, with index 0 = today
    increment_count = deque([ages.count(day) for day in range(CYCLE_TIMER)])
    new_increment_count = deque([0] * CYCLE_OFFSET)

    for day in range(days):
        new_fish_count = increment_count[0]
        total_fish_count += new_fish_count

        increment_count.rotate(-1)
        increment_count[CYCLE_TIMER - 1] += new_increment_count[0]

        new_increment_count.rotate(-1)
        new_increment_count[CYCLE_OFFSET - 1] = new_fish_count

    print(total_fish_count)


if __name__ == "__main__":
    input_file = Path(__file__).parent / INPUT_FILENAME
    input_line = input_file.read_text().strip()
    
    ages = [int(age) for age in input_line.split(",")]

    part1(ages, 80)
    part2(ages, 256)