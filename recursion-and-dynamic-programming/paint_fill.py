"""Implement the paint-fill function that one might see on many image editing
programs. That is, given a screen (represented by a two-dimensional array of colors),
a point, and a new color, fill in the surrounding area until ...
"""
from typing import List, Tuple
from collections import deque


def paint_fill(point: Tuple[int, int], matrix: List[List[int]], new_color: int):
    """DFS implementation"""
    visited = set()
    rows, cols = len(matrix), len(matrix[0])

    def traverse(idx: Tuple[int, int]):
        if idx not in visited:
            visited.add(idx)
            i, j = idx
            temp_color, matrix[i][j] = matrix[i][j], new_color
            for next_idx in get_neighbors(idx, rows, cols):
                nxt_i, nxt_j = next_idx
                if next_idx not in visited and temp_color == matrix[nxt_i][nxt_j]:
                    traverse(next_idx)

    traverse(point)


def paint_fill_v2(point: Tuple[int, int], matrix: List[List[int]], new_color: int):
    """BFS implementation"""
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    queue = deque()
    queue.append(point)
    visited.add(point)
    while queue:
        i, j = queue.popleft()
        temp_color, matrix[i][j] = matrix[i][j], new_color
        for next_idx in get_neighbors((i, j), rows, cols):
            nxt_i, nxt_j = next_idx
            if next_idx not in visited and temp_color == matrix[nxt_i][nxt_j]:
                matrix[nxt_i][nxt_j] = new_color # is this needed?
                visited.add(next_idx)
                queue.append(next_idx)


def get_neighbors(idx, rows, cols):
    i, j = idx
    if i > 0:
        yield i-1, j
    if j > 0:
        yield i, j-1
    if i+1 < rows:
        yield i+1, j
    if j+1 < cols:
        yield i, j+1


if __name__ == "__main__":
    map1 = [
        [1, 2, 1, 2],
        [1, 1, 1, 3],
        [2, 3, 2, 2]
    ]
    map2 = [
        [32, 2, 1, 22],
        [32, 22, 22, 22],
        [22, 22, 2, 2]
    ]

    paint_fill((1, 1), map1, color=10)
    print(map1)
    paint_fill((0, 1), map1, color=20)
    print(map1)

    paint_fill((0, 0), map2, color=10)
    print(map2)
    paint_fill((1, 1), map2, color=20)
    print(map2)
