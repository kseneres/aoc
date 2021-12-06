import pathlib
from collections import deque

INPUT_FILE="input"

def part1(ages: list[int], days: int):
    for day in range(80):
        count = ages.count(0)

        ages = [age - 1 if age > 0 else 6 for age in ages]
        ages = ages + [8] * count

        # print(f"day {day}: {ages}")

    print(len(ages))

def part2(ages: list[int], days: int):
    total_fish_count = len(ages)

    # queue for count of fish to spawn, rotated every day, with index 0 = today
    increment_count = deque([ages.count(day) for day in range(7)])
    new_increment_count = deque([0, 0])

    for day in range(days):
        # print(f"day: {day}: {count}")

        new_fish_count = increment_count[0]
        total_fish_count += new_fish_count

        increment_count[0] += new_increment_count[0]
        new_increment_count[0] = new_fish_count

        increment_count.rotate(-1)
        new_increment_count.rotate(-1)

    print(total_fish_count)


if __name__ == "__main__":
    input_line = pathlib.Path(INPUT_FILE).read_text().strip()
    ages = [int(age) for age in input_line.split(",")]

    part1(ages, 80)
    part2(ages, 256)