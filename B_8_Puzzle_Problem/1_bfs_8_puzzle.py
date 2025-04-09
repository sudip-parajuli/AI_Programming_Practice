from collections import deque

GOAL_STATE = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))  # 0 is the blank

def get_neighbors(state):
    neighbors = []
    rows, cols = 3, 3
    zero_r, zero_c = next((r, c) for r in range(3) for c in range(3) if state[r][c] == 0)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in directions:
        r, c = zero_r + dr, zero_c + dc
        if 0 <= r < rows and 0 <= c < cols:
            new_state = [list(row) for row in state]
            new_state[zero_r][zero_c], new_state[r][c] = new_state[r][c], new_state[zero_r][zero_c]
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors

def bfs(start):
    queue = deque([(start, [])])
    visited = set()
    visited.add(start)

    while queue:
        state, path = queue.popleft()
        if state == GOAL_STATE:
            return path + [state]
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [state]))
    return None

# Example run
if __name__ == "__main__":
    initial = ((1, 2, 3),
               (4, 0, 6),
               (7, 5, 8))

    result = bfs(initial)
    if result:
        print(f"Solution in {len(result)-1} steps:")
        for step in result:
            for row in step:
                print(row)
            print()
    else:
        print("No solution found.")
