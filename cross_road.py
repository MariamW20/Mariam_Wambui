import numpy as np
import random

# States: positions 0 to 4
positions = 5
actions = ['left', 'right']  # 0: left, 1: right
Q = np.zeros((positions, len(actions)))

# Parameters
episodes = 10
learning_rate = 0.8
gamma = 0.9
epsilon = 0.3

# To track the correct sequence: right → left → right
for episode in range(episodes):
    state = 0  # Always start at position 0
    sequence = []  # Track moves for this episode
    done = False

    while not done:
        # Choose action: epsilon-greedy
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, 1)
        else:
            action = np.argmax(Q[state])

        # Take action
        next_state = max(0, state - 1) if action == 0 else min(positions - 1, state + 1)
        sequence.append(action)

        # Reward logic: Only reward the exact pattern [1, 0, 1]
        if len(sequence) >= 3 and sequence[-3:] == [1, 0, 1]:
            reward = 10
            done = True
        else:
            reward = -1

        # Q-update
        Q[state, action] += learning_rate * (
            reward + gamma * np.max(Q[next_state]) - Q[state, action]
        )

        state = next_state

# Show final Q-table
print("Final Q-table:")
print(Q)

# Test agent
print("\nTesting agent for 'right → left → right' sequence:")
state = 0
sequence = []
steps = 0

while steps < 10:  # Max 10 steps to avoid infinite loop
    action = np.argmax(Q[state])
    next_state = max(0, state - 1) if action == 0 else min(positions - 1, state + 1)
    print(f"Step {steps}: Position {state} -> Action {actions[action]} -> {next_state}")
    sequence.append(action)
    state = next_state
    steps += 1

    if len(sequence) >= 3 and sequence[-3:] == [1, 0, 1]:
        print("\n Success: Correct sequence achieved!")
        break
