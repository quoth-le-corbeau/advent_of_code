import time
import pathlib
import re
from collections import defaultdict, deque


def sum_middle_pages(file_path: str) -> int:
    rules, updates = _parse_input(file=file_path)
    order_map = _get_order_map(rules)
    print(f"{order_map=}")
    middles = 0
    for update in updates:
        if len(update) == 0:
            continue
        if _is_ordered(list_to_check=update, order_map=order_map):
            print(f"{update} is an ordered update")
            middles += update[len(update) // 2]
    return middles


def _is_ordered(list_to_check: list[int], order_map: dict[int, int]) -> bool:
    idx_list = [order_map[n] for n in list_to_check if n in order_map]
    return sorted(idx_list) == idx_list


def _get_order_map(rules: list[tuple[int, int]]) -> dict[int, int]:
    ordered = []
    for rule in rules:
        x, y = rule
        if not (x in ordered or y in ordered):
            ordered += [x, y]
        if x in ordered and not y in ordered:
            index = ordered.index(x)
            ordered.insert(index + 1, y)
        if x not in ordered and y in ordered:
            index = ordered.index(y)
            ordered.insert(index, x)
        if x in ordered and y in ordered:
            x_index = ordered.index(x)
            y_index = ordered.index(y)
            if x_index > y_index:
                ordered.remove(x)
                ordered.insert(y_index, x)
            else:
                continue
    return {n: ordered.index(n) for n in ordered}


def _get_order_map_kahn(rules: list[tuple[int, int]]) -> dict[int, int]:
    rules = list(set(rules))

    graph = defaultdict(list)
    in_degree = defaultdict(int)
    nodes = set()

    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        nodes.add(x)
        nodes.add(y)

    for node in nodes:
        if node not in in_degree:
            in_degree[node] = 0

    print("Graph:", dict(graph))
    print("In-Degree:", dict(in_degree))

    queue = deque([node for node in nodes if in_degree[node] == 0])
    ordered = []

    while queue:
        node = queue.popleft()
        ordered.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(ordered) != len(nodes):
        print("Ordered nodes:", ordered)
        print("Remaining in-degrees:", {k: v for k, v in in_degree.items() if v > 0})
        raise ValueError(
            "Input rules contain a cycle, and a valid order cannot be determined."
        )

    return {node: index for index, node in enumerate(ordered)}


def _parse_input(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read()
        rules, updates = lines.split("\n\n")
        rules = [
            (int(rule.split("|")[0]), int(rule.split("|")[1]))
            for rule in rules.split("\n")
        ]
        updates = [
            list(map(int, re.findall(r"(\d+)", line))) for line in updates.split("\n")
        ]
        return rules, updates


START = time.perf_counter()
print(
    sum_middle_pages(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_5"
                / "eg.txt"
            )
        )
    )
)
print(f"TEST -> Elapsed {time.perf_counter() - START:2.4f} seconds.")

START = time.perf_counter()
print(
    sum_middle_pages(
        str(
            (
                pathlib.Path(__file__).resolve().parents[2]
                / "my_inputs/2024/day_5"
                / "input.txt"
            )
        )
    )
)
print(f"REAL -> Elapsed {time.perf_counter() - START:2.4f} seconds.")
