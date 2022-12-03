from pathlib import Path
import copy

INPUT_FILENAME="input"

class Grid:

    def __init__(self, grid: list[list[int]]):
        self.grid = copy.deepcopy(grid)
        self.flashed = [[False] * 10 for _ in range(10)]

    def increment_all(self): 
        for y in range(10): 
            for x in range(10):
                self.grid[y][x] += 1

    # update the tally for amount of increase for each point in the grid
    def increment_adjacent(self, increase_tally: list[list[int]], x: int, y: int):
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if i == y and j == x: 
                    continue

                if i >= 0 and i < 10 and j >= 0 and j < 10:
                    increase_tally[i][j] += 1

    def flash_updates(self) -> bool:
        increase_tally = [[0] * 10 for _ in range(10)]
        for y in range(10): 
            for x in range(10):
                if self.grid[y][x] > 9 and not self.flashed[y][x]:
                    self.increment_adjacent(increase_tally, x, y)
                    self.flashed[y][x] = True

        # update the grid with the flash increase 
        updated = False
        for y in range(10): 
            for x in range(10):
                self.grid[y][x] += increase_tally[y][x]
                if increase_tally[y][x] != 0: 
                    updated = True

        return updated

    # reset the energy levels in the grid to 0
    # and return the number of flashes
    def reset(self) -> int: 
        flash_count = 0
        for y in range(10): 
            for x in range(10):
                if self.grid[y][x] > 9:
                    flash_count +=1
                    self.grid[y][x] = 0

                self.flashed[y][x] = False

        return flash_count

    def step(self, print=False) -> int: 
        self.increment_all()

        increased = True
        while increased:
            increased = self.flash_updates()

        count = self.reset()

        if print:
            self.display()

        return count

    def is_synchronized(self) -> bool: 
        for y in range(10): 
            for x in range(10):
                if self.grid[y][x] != 0:
                    return False

        return True
        
    def display(self): 
        int_to_display_string = lambda i : f"\033[1m{i}\033[0m" if i == 0 else str(i)

        rows = ["".join([int_to_display_string(i) for i in row]) for row in self.grid]
        display_string = "\n".join(rows)

        print(display_string)
        print()

                
def part1(grid: Grid):
    total_flash_count = 0
    for step in range(100):
        # print(f"Step {step + 1}: ")
        total_flash_count += grid.step()

    print(total_flash_count)


def part2(grid: Grid):
    step = 0
    synchronized = False
    while not synchronized:
        # print(f"Step {step + 1}: ")
        step += 1

        grid.step()
        synchronized = grid.is_synchronized()

    print(step)


if __name__ == "__main__":
    input_file = Path(__file__).parent / INPUT_FILENAME
    input_lines = input_file.read_text().strip().split("\n")

    grid_contents = [[int(energy) for energy in line] for line in input_lines]

    part1(Grid(grid_contents))
    part2(Grid(grid_contents))