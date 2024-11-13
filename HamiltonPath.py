from utils import *


def is_valid_move(arr, x, y, visited):
    return 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] != ROAD_BLOCK and (x, y) not in visited


def find_hamiltonian_path(arr, x, y, path, visited):
    if len(path) == len(arr) * len(arr[0]) - sum(row.count(ROAD_BLOCK) for row in arr):
        return path

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if is_valid_move(arr, new_x, new_y, visited):
            visited.add((new_x, new_y))
            path.append((new_x, new_y))
            result = find_hamiltonian_path(arr, new_x, new_y, path, visited)
            if result:
                return result
            path.pop()
            visited.remove((new_x, new_y))
    return None


def HamiltonPath(arr):
    start_pos = None
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == START:
                start_pos = (i, j)
                break
        if start_pos:
            break

    if not start_pos:
        return None

    path = [start_pos]
    visited = set(path)
    return find_hamiltonian_path(arr, start_pos[0], start_pos[1], path, visited)
