from typing import List
from collections import deque


def printpath(path: List[int]) -> None:
    size = len(path)
    for i in range(size):
        print(path[i], end=" ")
    print()


def isNotVisited(x: int, path: List[int]) -> int:
    size = len(path)
    for i in range(size):
        if path[i] == x:
            return 0

    return 1


def findpaths(g: List[List[int]], src: int, dst: int, v: int) -> None:
    q = deque()
    path = []
    path.append(src)
    q.append(path.copy())

    while q:
        path = q.popleft()
        last = path[len(path) - 1]

        # If last vertex is the desired destination
        # then print the path
        if last == dst:
            printpath(path)

        # Traverse to all the nodes connected to
        # current vertex and push new path to queue
        for i in range(len(g[last])):
            if isNotVisited(g[last][i], path):
                newpath = path.copy()
                newpath.append(g[last][i])
                q.append(newpath)


# Driver code
if __name__ == "__main__":
    # Number of vertices
    v = 4
    g = [[] for _ in range(4)]

    # Construct a graph
    g[0].append(3)
    g[0].append(1)
    g[0].append(2)
    g[1].append(3)
    g[2].append(0)
    g[2].append(1)

    src = 2
    dst = 3
    print("path from src {} to dst {} are".format(src, dst))

    # Function for finding the paths
    findpaths(g, src, dst, v)
