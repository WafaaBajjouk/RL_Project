# Rubik's Cube Reinforcement Learning

This project aims to solve the Rubik's Cube using reinforcement learning techniques, specifically feature-based Q-learning and a pattern database to estimate optimal moves.

## Classes Overview

### `Agent`

The `Agent` class is responsible for the learning and decision-making process within the Rubik's Cube environment. Key features include:

- **Initialization:** Sets up the agent's Q-values, the starting state of the cube, and the list of possible actions.
- **Pattern Registration:** Uses `register_patterns` to initialize Q-values for different states based on the distance (in moves) from the solved state.
- **Reward Calculation:** Implements a `reward` function to evaluate the result of an action, considering factors like reaching the goal state, number of solved sides, and correctly placed pieces.
- **Max Reward Calculation:** The `max_reward` method calculates the highest possible reward from the next state, aiding in the Q-value update process.

### `State`

The `State` class represents the Rubik's Cube and includes methods for manipulating and evaluating its state. Key features include:

- **Initialization and Representation:** Initializes the cube with default or provided configurations and allows getting and setting of cube sides.
- **Cube Manipulation:** Provides methods to rotate (`turn_left`, `turn_right`, `turn_front`, `turn_back`, `turn_top`, `turn_bottom`) and flip the cube, essential for simulating the environment.
- **Goal State Check:** The `isGoalState` method checks if the cube is solved, determining the success of the agent's actions.

### Utility Functions (`utils.py`)

Utility functions assist in evaluating the cube's state and applying moves. Key features include:

- **State Evaluation:** Functions like `num_pieces_correct_side`, `num_solved_sides`, `num_crosses`, and `num_xs` assess different aspects of the cube’s state.
- **State Manipulation:** Functions such as `n_move_state`, `one_move_state`, `shuffle`, and `random_move` initialize the cube in various states and apply moves to it.
- **Move Execution:** The `move` function applies a specified action to a cube state and returns the resulting state.

---
