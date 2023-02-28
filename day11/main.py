from collections import namedtuple
from dataclasses import dataclass, field, replace
import dataclasses
import pathlib
import time
from typing import Dict, List, Set, Tuple

INPUT_FILE = "example"
# INPUT_FILE = "input"


@dataclass
class Operand:
    multiplicands: Dict[int, int]
    frequency: int = 1

    def multiply_by(self, value):
        for k in self.multiplicands.keys():
            if k == value:
                self.multiplicands[k] += 1

    def update_with_other(self, other: "Operand"):
        for key in self.multiplicands.keys():
            for other_key in other.multiplicands.keys():
                if key == other_key:
                    self.multiplicands[key] += other.multiplicands[other_key]

    def is_single(self) -> bool:
        return len(self.multiplicands) == 1

    def add_value_to_single(self, to_add):
        key, _ = self.multiplicands.popitem()
        self.multiplicands[key + to_add] = 1

    def __eq__(self, other: "Operand") -> bool:
        return set(self.multiplicands.keys()) == set(other.multiplicands.keys())


@dataclass
class Item:
    operands: List[Operand]

    def add_new_operand(self, to_add: int):
        self.operands.append(Operand({to_add: 1}))

    def reduce_operands(self):
        for i in range(len(self.operands) - 1):
            operand = self.operands[i]

            for j in range(i + 1, len(self.operands) - 1):
                other_operand = self.operands[j]

                if operand == other_operand:
                    operand.frequency += other_operand.frequency
                    self.operands.pop(j)


@dataclass
class Monkey:
    items: List[Item]

    operation: str
    right_operand: str

    test_divisible: int
    true_pass: int
    false_pass: int

    inspected_count = 0


def parse(puzzle_input: str) -> Dict[int, Monkey]:
    groups = [line for line in puzzle_input.split("\n\n")]

    monkeys = {}
    for group in groups:
        lines = group.split("\n")

        id = int(list(lines[0])[-2])

        items = lines[1].replace("Starting items: ", "").split(",")
        items = [int(item.strip()) for item in items]
        items = [Item([Operand({item: 1})]) for item in items]

        operation = lines[2].split()
        cmd, right = operation[4], operation[5]

        divisible_by = int(lines[3].split(" ")[-1])

        true = int(lines[4].split(" ")[-1])
        false = int(lines[5].split(" ")[-1])

        m = Monkey(items, cmd, right, divisible_by, true, false)
        monkeys[id] = m

    return monkeys


def part1(monkeys: Dict[int, Monkey]):
    for _ in range(20):
        for id in monkeys.keys():
            m = monkeys[id]

            for item in m.items:
                right_operand = item if m.right_operand == "old" else int(m.right_operand)
                if m.operation == "*":
                    result = item * right_operand
                if m.operation == "+":
                    result = item + right_operand

                result = result // 3
                test = result % m.test_divisible == 0

                if test:
                    monkeys[m.true_pass].items.append(result)
                else:
                    monkeys[m.false_pass].items.append(result)

            m.inspected_count += len(m.items)
            m.items.clear()

    for k, v in monkeys.items():
        print(k, v.inspected_count)

    counts = [m.inspected_count for m in monkeys.values()]
    counts.sort(reverse=True)
    first, second = counts[:2]
    monkey_business = first * second
    print(monkey_business)


def part2(monkeys: Dict[int, Monkey]):
    for round in range(20):
        for id in monkeys.keys():
            m = monkeys[id]

            # print()
            # print(f"round: {round}", id)

            for item in m.items:
                # print(id, item)

                if m.operation == "*":
                    if m.right_operand == "old":
                        # go through every operand and append all others (distribute)
                        # TODO: fix
                        for operand in item.operands:
                            for other_operand in item.operands:
                                operand.update_with_other(other_operand)
                    else:
                        # adjust every operand
                        for operand in item.operands:
                            operand.multiply_by(int(m.right_operand))

                if m.operation == "+":
                    to_add = int(m.right_operand)

                    if item.operands[-1].is_single():
                        # append to last operand
                        item.operands[-1].add_value_to_single(to_add)
                    else:
                        item.add_new_operand(to_add)

                # start: 53
                # i = 53 * 3
                # divisible by 13
                # no, next i = (53 * 3) + 8
                # divisible by 7
                # no, next i = ((53*3)+8) + 4 = (53*3)+12
                # divisible by 3
                # yes, next i = ((53*3)+12) + 5 = (53*3)+17
                # divisible by 17
                # no, next i = ((53*3)+17)*7 = 53*3*7 + 17*7
                # divisible by 5
                # no, next i =  (53*3*7 + 17*7) * 3 = 53*3*7*3 + 17*7*3
                # divisible by 13
                # no, next i = (53*3*7*3 + 17*7*3) + 8

                # (53*3*7*3 + 17*7*3) * (53*3*7*3 + 17*7*3)
                # divisible iff both sides are divisible

                # (53*3*7*3 + 17*7*3 + 8) * (53*3*7*3 + 17*7*3 + 8) = 13,719,616
                # (53*3*7*3)(53*3*7*3 + 17*7*3 + 8)
                # +(17*7*3)(53*3*7*3 + 17*7*3 + 8)
                # +8(53*3*7*3 + 17*7*3 + 8)

                # for x in range(len(item) - 1):
                #     item = item[x]
                #     repeats = 1

                #     for y in range(x + 1, len(item) - 1):
                #         other_operand = item[y]
                #         if item == other_operand:
                #             print("repeat", item, other_operand)
                #             # item.pop(y)
                #             repeats += 1

                #     if repeats > 1:
                #         item.add(repeats)
                #         print("repeat new", item)

                # item.reduce_operands()

                check = True
                for operand in item.operands:
                    if not (
                        any(i % m.test_divisible == 0 for i in operand.multiplicands.keys())
                        or operand.frequency % m.test_divisible == 0
                    ):
                        check = False

                # total = 0
                # for operand in item:
                #     total_mult = 1
                #     for i in operand:
                #         total_mult *= i
                #     total += total_mult
                # check = total % m.test_divisible == 0

                monkeys[m.true_pass if check else m.false_pass].items.append(item)

            m.inspected_count += len(m.items)
            m.items.clear()

    for k, v in monkeys.items():
        print(k, v.inspected_count)

    counts = [m.inspected_count for m in monkeys.values()]
    counts.sort(reverse=True)
    first, second = counts[:2]
    monkey_business = first * second
    print(monkey_business)


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text()
    monkeys_1 = parse(puzzle_input)
    monkeys_2 = parse(puzzle_input)

    # print(part1(monkeys_1))
    print(part2(monkeys_2))
