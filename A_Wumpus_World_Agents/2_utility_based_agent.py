"""
A Utility-Based Agent selects actions to maximize a utility function.
"""

def utility_based_agent(percept):
    utilities = {
        'grab': 100,
        'shoot': -10,
        'move_backward': -5,
        'move_forward': 1
    }

    if 'glitter' in percept:
        return 'grab'
    elif 'stench' in percept:
        return 'shoot'
    elif 'breeze' in percept:
        return 'move_backward'
    else:
        return 'move_forward'

# Simulating with utilities
percepts_list = [
    ['glitter'],
    ['stench'],
    ['breeze'],
    []
]

for i, p in enumerate(percepts_list):
    action = utility_based_agent(p)
    print(f"Step {i+1}: Percepts: {p} -> Action: {action}")
