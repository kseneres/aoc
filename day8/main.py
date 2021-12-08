from pathlib import Path
from collections import deque
import sys

INPUT_FILENAME="input"

def part1(input_data: list[list[str]]):
    output_data = [data[1].split(" ") for data in input_data]

    count = 0
    known_digit_sizes = [2, 3, 4, 7]
    for output in output_data:
        count += sum(len(digit) in known_digit_sizes for digit in output)

    print(count)


def part2(input_data: list[list[str]]):

    def get_output_value(data: list[str]) -> int: 
        patterns = [set(d) for d in data[0].split(" ")]
        output_patterns = [set(d) for d in data[1].split(" ")]

        one = next(p for p in patterns if len(p) == 2)
        four = next(p for p in patterns if len(p) == 4)
        seven = next(p for p in patterns if len(p) == 3)
        eight = next(p for p in patterns if len(p) == 7)

        two_three_five = [p for p in patterns if len(p) == 5]
        three = next(d for d in two_three_five if one.issubset(d))
        two = next(d for d in two_three_five if len(d.difference(four)) == 3)
        five = next(d for d in two_three_five if d != three and d != two)

        zero_six_nine = [p for p in patterns if len(p) == 6]
        nine = next(d for d in zero_six_nine if four.issubset(d))
        zero = next(d for d in zero_six_nine if one.issubset(d) and d != nine)
        six = next(d for d in zero_six_nine if d != zero and d != nine)

        digits = [zero, one, two, three, four, five, six, seven, eight, nine]
        numbers = [next(i for i, v in enumerate(digits) if o == v) for o in output_patterns]
        output_value = sum([numbers[i] * 10**(3-i) for i in range(4)])

        return output_value
    
    total = sum([get_output_value(data) for data in input_data])
    print(total)


if __name__ == "__main__":
    input_file = Path(__file__).parent / INPUT_FILENAME
    input_lines = input_file.read_text().strip().split("\n")

    input_data = [line.split(" | ") for line in input_lines] 

    #  aaaa
    # b    c  
    # b    c  
    #  dddd    
    # e    f  
    # e    f 
    #  gggg    

    part1(input_data)
    part2(input_data)