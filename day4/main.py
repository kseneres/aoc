import pathlib
from dataclasses import dataclass, field
from typing import List, Tuple

INPUT_FILE="input"

@dataclass
class BingoBoard:
    # size 25, each group of 5 is one row
    numbers: list[int]

    # indexes of numbers in the list that have been called out
    punched_numbers: list[int] = field(default_factory=list)

    score: int = 0

    def calculate_score(self, last_input: int) -> int:
        total = 0
        for i, n in enumerate(self.numbers):
            if i not in self.punched_numbers:
                total += n

        self.score = total * last_input

    def process(self, input: int) -> bool: 
        column_match = row_match = False

        for i, n in enumerate(self.numbers):
            if n == input: 
                self.punched_numbers.append(i)

        self.punched_numbers.sort()
        
        if len(self.punched_numbers) > 5:
            # check column match
            for i in range(0, 5):
                columns = list(range(i, 25, 5))
                column_match = all(n in self.punched_numbers for n in columns)

                if column_match:
                    break
            
            # check row match
            for i in range(0, 25, 5):
                rows = list(range(i, i+5))
                row_match = all(n in self.punched_numbers for n in rows)

                if row_match:
                    break
        
        if column_match or row_match:
            self.calculate_score(input)

        return column_match or row_match

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