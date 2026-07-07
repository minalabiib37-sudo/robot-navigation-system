"""
Autonomous Robot Navigation System
Author: Mina Labib
"""

from path_planning import AStarPlanner
from simulator import Simulator

def main():
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
    ]

    start = (0, 0)
    goal = (4, 4)

    planner = AStarPlanner(grid)
    path = planner.find_path(start, goal)

    print("=== Autonomous Robot Navigation System ===")
    print("Start:", start)
    print("Goal:", goal)
    print("Path:", path)
    print("\nGrid Visualization:\n")

    simulator = Simulator(grid, path)
    simulator.display()

if __name__ == "__main__":
    main()
