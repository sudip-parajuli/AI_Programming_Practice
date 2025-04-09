
import copy

# Initial and goal states
initial_state = [['C', 'B'], ['A'], []]
goal_state = [['A', 'B', 'C'], [], []]

def heuristic(state):
    """Heuristic: Number of misplaced blocks compared to goal."""
    misplaced = 0
    for i in range(len(goal_state)):
        for j in range(min(len(goal_state[i]), len(state[i]))):
            if goal_state[i][j] != state[i][j]:
                misplaced += 1
        # Count extra blocks
        if len(state[i]) > len(goal_state[i]):
            misplaced += len(state[i]) - len(goal_state[i])
    return misplaced

def get_neighbors(state):
    """Generate all valid next moves by moving top block to another stack."""
    neighbors = []
    for i in range(len(state)):
        if not state[i]:  # Skip empty stacks
            continue
        for j in range(len(state)):
            if i != j:
                # Move top block from stack i to stack j
                new_state = copy.deepcopy(state)
                block = new_state[i].pop()
                new_state[j].append(block)
                neighbors.append(new_state)
    return neighbors

def hill_climbing(start_state):
    current = start_state
    current_h = heuristic(current)

    while True:
        neighbors = get_neighbors(current)
        neighbor_h = [(heuristic(n), n) for n in neighbors]
        neighbor_h.sort(key=lambda x: x[0])

        best_h, best_state = neighbor_h[0]

        if best_h >= current_h:
            return current  # Return local best (could be goal or local minima)

        current = best_state
        current_h = best_h

# Utility function to print states
def print_state(state):
    for stack in state:
        print(stack)
    print("-" * 20)

# Run the algorithm
if __name__ == "__main__":
    print("Initial State:")
    print_state(initial_state)

    final_state = hill_climbing(initial_state)

    print("Final State:")
    print_state(final_state)

    if final_state == goal_state:
        print("Goal reached!")
    else:
        print("Stuck in local minima. Goal not reached.")
