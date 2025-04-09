import heapq

# Define the graph as an adjacency list with costs
graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 7)],
    'D': [('G', 3)],
    'G': []
}

# Heuristic values for each node (Estimated cost to goal)
heuristics = {
    'S': 7,
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 2,
    'G': 0
}

def best_first_search(start, goal):
    visited = set()
    pq = []
    heapq.heappush(pq, (heuristics[start], [start]))

    while pq:
        heuristic, path = heapq.heappop(pq)
        current = path[-1]
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                heapq.heappush(pq, (heuristics[neighbor], new_path))

    return None

# Example run
if __name__ == "__main__":
    start_node = 'S'
    goal_node = 'G'
    result = best_first_search(start_node, goal_node)

    if result:
        print("Path found:", " -> ".join(result))
    else:
        print("No path found.")
