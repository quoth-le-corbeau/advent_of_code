import heapq, math, sys

INFINITY = float("inf")


class Node:
    def __init__(
        self,
        position: tuple[int, int],
        f_score: float = INFINITY,
        g_score: int = INFINITY,
        parent=None,
    ) -> None:
        self.position = position
        self.f_score = f_score
        self.g_score = g_score
        self.parent = parent

    def __lt__(self, other):
        return self.f_score < other.f_score


class AStar:
    def __init__(
        self,
        start: tuple[int, int],
        # TODO: check typing here
        grid: list[list[str]],
        height: int,
        width: int,
    ) -> None:
        self.start = start
        self.grid = grid
        self.height = height
        self.width = width

    def heuristic_manhattan(self, end_node: Node) -> int:
        x1, y1 = self.start
        x2, y2 = end_node.position
        return abs(x1 - x2) + abs(y1 - y2)

    def node_neighbours(self, node: Node) -> dict[tuple[int, int], str]:
        """check neighbour is not a wall and is not outside the grid"""
        x, y = node.position
        potential_neighbour_positions = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
        neighbours = dict()
        for potential_neighbour_position in potential_neighbour_positions:
            if (
                0 <= potential_neighbour_position[0] < self.width
                and 0 <= potential_neighbour_position[1] < self.height
            ):
                neighbours[potential_neighbour_position] = self.get_grid_value(
                    position=potential_neighbour_position
                )
        return neighbours

    def get_grid_value(self, position: tuple[int, int]) -> str:
        return self.grid[position[1]][position[0]]

    def get_path(self, end_node: Node) -> list[tuple[int, int]]:
        current = end_node
        path = list()
        while current.position != self.start:
            path.append(current.position)
            current = current.parent
        path.append(self.start)
        return path[::-1]

    @staticmethod
    def neighbour_is_not_wall(current_letter: str, neighbour_letter: str) -> bool:
        if current_letter not in ["S", "E"]:
            return abs(ord(current_letter) - ord(neighbour_letter)) < 2
        else:
            return True

    def compute_path(self, end_node: Node) -> list[tuple[int, int]]:
        open_list = list()
        closed_list = list()
        node_dict = dict()
        current_node = Node(
            position=self.start,
            f_score=self.heuristic_manhattan(end_node=end_node),
            g_score=0,
        )
        heapq.heappush(open_list, current_node)
        while len(open_list) > 0:
            current_node = heapq.heappop(open_list)
            if current_node.position == end_node.position:
                return self.get_path(current_node)
            else:
                closed_list.append(current_node)
                neighbours: list[Node] = list()
                node_neighbours_dict = self.node_neighbours(node=current_node)
                for coordinate_to_check, letter in node_neighbours_dict.items():
                    if (
                        coordinate_to_check not in node_dict.keys()
                        and self.neighbour_is_not_wall(
                            current_letter=self.get_grid_value(
                                position=current_node.position
                            ),
                            neighbour_letter=letter,
                        )
                    ):
                        node_dict[coordinate_to_check] = Node(coordinate_to_check)
                        neighbours.append(node_dict[coordinate_to_check])

                for neighbour in neighbours:
                    new_g_score = current_node.g_score + 1
                    if neighbour in open_list and new_g_score < neighbour.g_score:
                        open_list.remove(neighbour)
                    if new_g_score < neighbour.g_score and neighbour in closed_list:
                        closed_list.remove(neighbour)
                    if neighbour not in open_list and neighbour not in closed_list:
                        neighbour.g_score = new_g_score
                        neighbour.f_score = (
                            neighbour.g_score
                            + self.heuristic_manhattan(end_node=neighbour)
                        )
                        neighbour.parent = current_node
                        heapq.heappush(open_list, neighbour)
                    heapq.heapify(open_list)
        return self.get_path(current_node)
