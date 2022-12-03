import pathlib
from dataclasses import dataclass, field
from typing import List, Tuple

INPUT_FILE="input"

@dataclass
class BingoBoard:
    # size 25, each group of 5 is one row
    numbers: list[int]
    punched: list[bool] = field(default_factory=lambda: [False] * 25)

    score: int = 0

    def calculate_score(self, last_input: int) -> int:
        total = 0
        for i, n in enumerate(self.numbers):
            if not self.punched[i]:
                total += n

        self.score = total * last_input

    def process(self, input: int) -> bool: 
        column_match = row_match = False

        for i, n in enumerate(self.numbers):
            if n == input: 
                self.punched[i] = True

        for i in range(0, 5):
            offset = i * 5 
            row_match = all(self.punched[offset:offset + 5])
            column_match = all(self.punched[i:25:5])

            if column_match or row_match:
                self.calculate_score(input)
                return True

        return False

    def reset(self):
        self.punched_numbers = []
        self.score = 0


def part1(input_numbers: List[int], cards: List[BingoBoard]):
    for input in input_numbers:
        for card in cards:
            if card.process(input):
                print(card)
                return


def part2(input_numbers: List[int], cards: List[BingoBoard]):
    winning_card_count = 0

    for input in input_numbers:
        for card in cards:
            # skip cards that are already complete with a score
            if card.score != 0: 
                continue
            
            if card.process(input):
                winning_card_count += 1

            if winning_card_count == len(cards):
                print(card)
                return
                

def process_input(lines: List[str]) -> Tuple[List[int], List[BingoBoard]]:
    input_numbers = [int(n) for n in lines[0].split(",")]
    cards: List[BingoBoard] = []

    # process bingo boards
    for i in range(2, len(lines), 6):
        rows = [row.split() for row in lines[i:i+5]]
        flat_list = [int(n) for row in rows for n in row]
        cards.append(BingoBoard(flat_list))

    return input_numbers, cards

if __name__ == "__main__":
    lines = pathlib.Path(INPUT_FILE).read_text().strip().split("\n")
    input_numbers, cards = process_input(lines)

    part1(input_numbers, cards)

    for card in cards:
        card.reset()

    part2(input_numbers, cards)