from pathlib import Path
from collections import deque
import sys

INPUT_FILENAME="input"

def part1(positions: list[int]):
    total_positions = len(positions)
    best_fuel_cost = sys.maxsize

    for target_position in range(total_positions):
        deltas = [abs(p - target_position) for p in positions]
        fuel_cost = sum(deltas)

        best_fuel_cost = min(best_fuel_cost, fuel_cost)

    print(best_fuel_cost)


def part2(positions: list[int]):
    total_positions = len(positions)
    best_fuel_cost = sys.maxsize

    # lookup table for fuel cost per given delta
    UNKNOWN_COST = -1
    max_delta = abs(max(positions) - min(positions))
    step_costs = [UNKNOWN_COST] * (max_delta + 1)

    for target_position in range(total_positions):
        fuel_cost = 0
        for crab_position in positions:
            delta = abs(crab_position - target_position)

            if step_costs[delta] == UNKNOWN_COST:
                step_costs[delta] = sum([i + 1 for i in range(delta)])

            fuel_cost += step_costs[delta]

        best_fuel_cost = min(best_fuel_cost, fuel_cost)

    print(best_fuel_cost)

if __name__ == "__main__":
    input_file = Path(__file__).parent / INPUT_FILENAME
    input_line = input_file.read_text().strip()
    
    positions = [int(position) for position in input_line.split(",")]

    part1(positions)
    part2(positions)