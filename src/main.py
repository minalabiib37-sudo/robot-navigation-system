"""
Autonomous Robot Navigation System
Author: Mina Labib
"""

import time

class Robot:

    def __init__(self):
        self.position = (0, 0)

    def detect_obstacle(self):
        print("Scanning for obstacles...")
        time.sleep(1)
        return False

    def plan_path(self):
        print("Planning optimal path...")
        time.sleep(1)

    def move(self):
        print("Robot moving forward...")
        self.position = (self.position[0] + 1, self.position[1])

robot = Robot()

print("=== Autonomous Navigation Started ===")

for i in range(5):

    if robot.detect_obstacle():
        print("Obstacle detected!")
        robot.plan_path()

    robot.move()

print("Destination reached.")
