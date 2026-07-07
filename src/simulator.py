"""
Grid-based robot navigation simulator.
"""

class Simulator:
    def __init__(self, grid, path):
        self.grid = grid
        self.path = path

    def display(self):
        for row_index, row in enumerate(self.grid):
            line = ""

            for col_index, cell in enumerate(row):
                position = (row_index, col_index)

                if position == self.path[0]:
                    line += "S "
                elif position == self.path[-1]:
                    line += "G "
                elif position in self.path:
                    line += "* "
                elif cell == 1:
                    line += "# "
                else:
                    line += ". "

            print(line)
