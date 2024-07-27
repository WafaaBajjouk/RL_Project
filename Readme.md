# Rubik's Cube Solver using Reinforcement Learning

This project aims to solve the Rubik's Cube using feature-based Q-Learning and a pattern database. The algorithm quickly estimates the best moves by recording the minimum number of moves required to solve specific parts or patterns of the cube.

## Overview

### `Agent` Class
- **Purpose**: Manages the learning and decision-making process.
- **Key Features**:
  - **Initialization**: Sets up Q-values, starting state, and possible actions.
  - **Pattern Registration**: Initializes Q-values based on the distance from the solved state.
  - **Reward Calculation**: Provides rewards based on solved sides and correct piece placements.
  - **Max Reward Calculation**: Determines the highest possible reward for the next state.

### `State` Class
- **Purpose**: Represents the Rubik's Cube and provides methods for manipulation and evaluation.
- **Key Features**:
  - **Initialization**: Sets up the cube with default or provided configurations.
  - **Cube Manipulation**: Offers methods to rotate and flip the cube.
  - **Goal State Check**: Determines if the cube is solved.

### Utility Functions (`utils.py`)
- **Purpose**: Assist in evaluating and manipulating the cube's state.
- **Key Features**:
  - **State Evaluation**: Functions to assess solved sides, correct pieces, crosses, and X patterns.
  - **State Manipulation**: Functions to shuffle the cube and apply random or specific moves.
  - **Move Execution**: Applies specified actions to a cube state and returns the resulting state.
