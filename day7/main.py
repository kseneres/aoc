from collections import namedtuple
from dataclasses import dataclass
import pathlib
from typing import Dict, List, Tuple

INPUT_FILE = "example"
INPUT_FILE = "input"


class File:
    def __init__(self, name: str, size: int, parent: "File"):
        self.name = name
        self.size = size

        self.isDir = False
        self.parent = parent
        self.children: Dict[str, File] = {}

        # get parents to determine full path
        parents: List[str] = []
        node = parent
        while node:
            parents.append(node.name)
            node = node.parent

        self.id = "/".join(parents[::-1]) + "/" + name
        self.depth = len(parents)

    def add_child(self, file: "File"):
        self.children[file.name] = file

    def calculate_size(self):
        if self.isDir and self.size == 0:
            self.size = sum([f.size for f in self.children.values()])

    def __str__(self):
        type = "dir" if self.isDir else "file"
        return f"{self.id} ({type}, size={self.size})"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other: "File"):
        return self.id == other.id


def parse(puzzle_input: str) -> str:
    parent: File = None
    current_dir: File = None
    files: set[File] = set()

    for line in puzzle_input.split("\n"):
        if line.startswith("$ cd"):
            dir_name = line.split(" ")[2]

            if dir_name == "..":
                current_dir = current_dir.parent
            else:
                if current_dir:
                    current_dir = current_dir.children[dir_name]
                else:
                    current_dir = File(dir_name, 0, parent)
                    files.add(current_dir)

                current_dir.isDir = True

        elif not line.startswith("$ ls"):
            size, file_name = line.split(" ")
            file = File(file_name, int(size) if size != "dir" else 0, current_dir)

            current_dir.add_child(file)
            files.add(file)

    return list(files)


def part1(files: List[File]):
    total = 0
    sorted_files = sorted(files, key=lambda f: f.depth, reverse=True)

    for file in sorted_files:
        if file.parent:
            file.parent.calculate_size()

        if file.isDir and file.size <= 100000:
            total += file.size

    return total


def part2(files: List[File]):
    TOTAL_SIZE = 70000000
    MIN_DISK_SPACE = 30000000

    directory_sizes = [file.size for file in files if file.isDir]
    directory_sizes.sort()

    root_size = directory_sizes[-1]
    for size in directory_sizes:
        delta = TOTAL_SIZE - root_size + size
        if delta >= MIN_DISK_SPACE:
            return size


if __name__ == "__main__":
    puzzle_input = pathlib.Path(INPUT_FILE).read_text()
    files = parse(puzzle_input)

    print(part1(files))
    print(part2(files))