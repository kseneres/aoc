from pathlib import Path

# Reference:
# https://www.python.org/doc/essays/graphs/

INPUT_FILENAME="input"

def is_start(label: str) -> bool:
    return label == "start"
    
def is_end(label: str) -> bool:
    return label == "end"

def is_big(label: str) -> bool:
    return label.isupper()

def is_small(label: str) -> bool:
    return label.islower()


def part1(cave_graph: dict[str, list[str]]):

    def find_all_paths(graph, start, end, path=[]):
        path: list[str] = path + [start]

        if start == end:
            return [path]
        if start not in graph:
            return []
        
        paths = []
        for node in graph[start]:
            if node not in path or is_big(node):
                new_paths = find_all_paths(graph, node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)

        return paths

    paths = find_all_paths(cave_graph, "start", "end")
    print(len(paths))


def part2(cave_graph: dict[str, list[str]]):

    def find_all_paths(graph, start, end, path=[]):
        path: list[str] = path + [start]

        if start == end:
            return [path]
        if start not in graph:
            return []
        
        paths = []
        for node in graph[start]:
            if node not in path or is_big(node) or (node == target_node and path.count(node) < 2):
                new_paths = find_all_paths(graph, node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)

        return paths

    target_nodes = [node for node in cave_graph.keys() if is_small(node) and not is_start(node)]

    all_paths = []
    for target_node in target_nodes:
        paths = find_all_paths(cave_graph, "start", "end")
        all_paths.extend(paths)

    all_paths = [",".join(path) for path in all_paths]
    all_paths = set(all_paths)
    print(len(all_paths))


def get_cave_graph(input_lines: list[str]) -> dict[str, list[str]]:
    cave_graph: dict[str, list[str]] = {}

    for cave_connection in input_lines:
        a, b = cave_connection.split("-")

        if a in cave_graph:
            cave_graph[a].append(b)
        else:
            cave_graph[a] = [b]

        if b in cave_graph:
            cave_graph[b].append(a)
        else:
            cave_graph[b] = [a]

    return cave_graph

if __name__ == "__main__":
    input_file = Path(__file__).parent / INPUT_FILENAME
    input_lines = input_file.read_text().strip().split("\n")

    cave_graph = get_cave_graph(input_lines)
    part1(cave_graph)
    part2(cave_graph)