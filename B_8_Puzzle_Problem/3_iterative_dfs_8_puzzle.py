# 3_8puzzle_iddfs.py

GOAL_STATE = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))

def get_neighbors(state):
    neighbors = []
    rows, cols = 3, 3
    zero_r, zero_c = next((r, c) for r in range(3) for c in range(3) if state[r][c] == 0)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        r, c = zero_r + dr, zero_c + dc
        if 0 <= r < rows and 0 <= c < cols:
            new_state = [list(row) for row in state]
            new_state[zero_r][zero_c], new_state[r][c] = new_state[r][c], new_state[zero_r][zero_c]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def dls(state, goal, limit, path, visited):
    if state == goal:
        return path + [state]
    if limit <= 0:
        return None
    visited.add(state)
    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            result = dls(neighbor, goal, limit - 1, path + [state], visited)
            if result:
                return result
    return None

def iddfs(start, goal):
    for depth in range(1, 31):  # depth limit
        visited = set()
        result = dls(start, goal, depth, [], visited)
        if result:
            return result
    return None

# Example run
if __name__ == "__main__":
    initial = ((1, 2, 3),
               (4, 0, 6),
               (7, 5, 8))

    result = iddfs(initial, GOAL_STATE)
    if result:
        print(f"Solution in {len(result)-1} steps:")
        for step in result:
            for row in step:
                print(row)
            print()
    else:
        print("No solution found.")
