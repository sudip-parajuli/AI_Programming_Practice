"""
A Simple Reflex Agent in Wumpus World
- It reacts based on current percepts.
- No internal memory or reasoning about the environment.
"""

def simple_reflex_agent(percept):
    """
    Rules:
    - If stench -> shoot
    - If glitter -> grab
    - If breeze -> move opposite
    - Else -> move forward
    """
    if 'glitter' in percept:
        return 'grab'
    elif 'stench' in percept:
        return 'shoot'
    elif 'breeze' in percept:
        return 'move_backward'
    else:
        return 'move_forward'

# Simulating the environment
percepts_list = [
    ['breeze'],
    ['stench'],
    ['glitter'],
    [],
    ['stench', 'breeze']
]

for i, percepts in enumerate(percepts_list):
    action = simple_reflex_agent(percepts)
    print(f"Step {i+1}: Percepts: {percepts} -> Action: {action}")
