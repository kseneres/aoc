from pathlib import Path
from typing import NamedTuple
from collections import Counter

INPUT_FILENAME="input"

def part1(template: str, rules: dict[str, str]):
    new_polymer = template

    for step in range(10):
        polymer = new_polymer

        inserts = {}
        for i in range(len(polymer) - 1):
            pair = polymer[i] + polymer[i + 1]
            if pair in rules:
                inserts[i] = rules[pair]

        new_polymer = ""
        for i in range(len(polymer)):
            new_polymer += polymer[i]
            if i in inserts:
                new_polymer += inserts[i]

    counts = Counter(new_polymer).most_common()
    most_common = counts[0]
    least_common = counts[len(counts) - 1]
    print(f"{most_common}, {least_common}, {most_common[1] - least_common[1]}")


def part2(template: str, rules: dict[str, str]):
    pair_counts: dict[str, int] = {}
    for i in range(len(template) - 1):
        pair = template[i] + template[i + 1]
        pair_counts[pair] = pair_counts.get(pair, 0) + 1
        
    char_count = {}
    for c in template:
        char_count[c] = char_count.get(c, 0) + 1

    for step in range(40):
        pair_count_updates = {}
        for pair in pair_counts.keys():
            if pair in rules:
                insert_char = rules[pair]
                char_count[insert_char] = char_count.get(insert_char, 0) + pair_counts[pair]
                
                new_pair_1 = pair[0] + insert_char
                new_pair_2 = insert_char + pair[1]

                pair_count_updates[new_pair_1] = pair_count_updates.get(new_pair_1, 0) + pair_counts[pair] 
                pair_count_updates[new_pair_2] = pair_count_updates.get(new_pair_2, 0) + pair_counts[pair] 
                pair_count_updates[pair] = pair_count_updates.get(pair, 0) - pair_counts[pair]

        for key, value in pair_count_updates.items():
            pair_counts[key] = pair_counts.get(key, 0) + value

    counts = Counter(char_count).most_common()
    most_common = counts[0]
    least_common = counts[len(counts) - 1]
    print(f"{most_common}, {least_common}, {most_common[1] - least_common[1]}")


if __name__ == "__main__":
    input_file = Path(__file__).parent / INPUT_FILENAME
    input_lines = input_file.read_text().strip().split("\n")

    polymer_template = input_lines[0]
    pair_insertion_rules = [line for line in input_lines if line.find("->") > 0]

    rules: dict[str, str] = {}
    for rule in pair_insertion_rules:
        pair, insert = rule.split(" -> ")
        rules[pair] = insert
    
    part1(polymer_template, rules)
    part2(polymer_template, rules)