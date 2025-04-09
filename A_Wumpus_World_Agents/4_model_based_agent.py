
"""
A Model-Based Agent uses memory of past percepts.
"""

class ModelBasedAgent:
    def __init__(self):
        self.has_gold = False
        self.visited = set()

    def act(self, location, percept):
        self.visited.add(location)

        if 'glitter' in percept:
            self.has_gold = True
            return 'grab'
        elif self.has_gold:
            return 'climb'
        elif 'breeze' in percept or 'stench' in percept:
            return 'backtrack'
        else:
            return 'move_forward'

# Simulation
agent = ModelBasedAgent()
steps = [
    ((0, 0), ['glitter']),
    ((0, 1), []),
    ((1, 1), ['breeze']),
    ((1, 2), [])
]

for i, (loc, p) in enumerate(steps):
    action = agent.act(loc, p)
    print(f"Step {i+1}: Location: {loc}, Percepts: {p} -> Action: {action}")
