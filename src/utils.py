"""
Utility functions for the autonomous robot navigation system.
"""

import math


def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt(
        (point2[0] - point1[0]) ** 2 +
        (point2[1] - point1[1]) ** 2
    )


def is_goal_reached(robot_position, goal_position, tolerance=0.5):
    """Return True if the robot is within tolerance of the goal."""
    return calculate_distance(robot_position, goal_position) <= tolerance
