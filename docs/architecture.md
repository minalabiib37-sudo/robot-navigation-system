# System Architecture

The Autonomous Robot Navigation System is organized into modular components:

## Main Components

- `main.py` — Starts the robot navigation simulation.
- `path_planning.py` — Implements the A* path planning algorithm.
- `navigation.py` — Handles navigation logic.
- `obstacle_detection.py` — Simulates obstacle detection.
- `utils.py` — Provides helper functions.
- `config.py` — Stores project settings.

## Workflow

1. Load the grid environment.
2. Set the robot start and goal positions.
3. Detect obstacles.
4. Use A* search to calculate the shortest path.
5. Output the final navigation path.
