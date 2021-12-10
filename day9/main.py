from pathlib import Path
from collections import deque
import sys

INPUT_FILENAME="input"

def part1(cave_map: list[list[int]]):
    low_points = []

    for y in range(len(cave_map)):
        for x in range(len(cave_map[y])):
            row = cave_map[y]
            height = row[x]

            # check if boundaries are lower
            if x > 0 and row[x - 1] <= height: 
                continue
            if x < len(row) - 1 and row[x + 1] <= height:
                continue
            if y > 0 and cave_map[y - 1][x] <= height:
                continue 
            if y < len(cave_map) - 1 and cave_map[y + 1][x] <= height:
                continue

            low_points.append(height)

    answer = sum([point + 1 for point in low_points])
    print(answer)


def part2(cave_map: list[list[int]]):

    def get_higher_positions(current, previous):
        (x, y) = current

        row = cave_map[y]
        height = row[x]

        if height == 9:
            return []

        low_points = [(x, y)]
        if x > 0 and row[x - 1] >= height and (previous != (x - 1, y)): 
            low_points += get_higher_positions((x - 1, y), (x, y))
        if x < len(row) - 1 and row[x + 1] >= height and (previous != (x + 1, y)):
            low_points += get_higher_positions((x + 1, y), (x, y))

        if y > 0 and cave_map[y - 1][x] >= height and (previous != (x, y - 1)):
            low_points += get_higher_positions((x, y - 1), (x, y))
        if y < len(cave_map) - 1 and cave_map[y + 1][x] >= height and (previous != (x, y + 1)):
            low_points += get_higher_positions((x, y + 1), (x, y))

        return low_points

    basins = []
    for y in range(len(cave_map)):
        for x in range(len(cave_map[y])):
            basin = get_higher_positions((x, y), (x, y))

            # use set to remove duplicates
            basins.append(set(basin))

    basin_sizes = [len(basin) for basin in basins]

    basin_sizes.sort()
    largest_basins = basin_sizes[-3:]
    answer = largest_basins[0] * largest_basins[1] * largest_basins[2]
    print(answer)


if __name__ == "__main__":
    input_file = Path(__file__).parent / INPUT_FILENAME
    input_lines = input_file.read_text().strip().split("\n")

    cave_map = [[int(i) for i in line] for line in input_lines]

    part1(cave_map)
    part2(cave_map)