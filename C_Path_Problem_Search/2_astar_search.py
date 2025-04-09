
import heapq

# Define the graph with neighbors and their costs
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 7)],
    'D': [('G', 3)],
    'G': []
}

# Heuristic estimate to goal (straight-line distance)
heuristics = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 2,
    'G': 0
}

def a_star_search(start, goal):
    pq = []
    heapq.heappush(pq, (heuristics[start], 0, [start]))  # (f(n), g(n), path)
    visited = set()

    while pq:
        f, cost_so_far, path = heapq.heappop(pq)
        current = path[-1]

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_cost = cost_so_far + cost
                f_score = new_cost + heuristics[neighbor]
                new_path = path + [neighbor]
                heapq.heappush(pq, (f_score, new_cost, new_path))

    return None

# Example run
if __name__ == "__main__":
    start_node = 'S'
    goal_node = 'G'
    result = a_star_search(start_node, goal_node)

    if result:
        print("Optimal path found:", " -> ".join(result))
    else:
        print("No path found.")
