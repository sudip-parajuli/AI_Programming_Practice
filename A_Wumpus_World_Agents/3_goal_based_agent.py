"""
A Goal-Based Agent plans actions to reach a defined goal.
"""

GOAL = 'get_gold'

def goal_based_agent(percept, has_gold=False):
    if not has_gold and 'glitter' in percept:
        return 'grab'
    elif has_gold:
        return 'climb'
    elif 'breeze' in percept or 'stench' in percept:
        return 'avoid'
    else:
        return 'explore'

# Simulate steps
steps = [
    (['glitter'], False),
    ([], True),
    (['breeze'], False),
    ([], False)
]

for i, (p, has_gold) in enumerate(steps):
    action = goal_based_agent(p, has_gold)
    print(f"Step {i+1}: Percepts: {p}, Has gold: {has_gold} -> Action: {action}")
