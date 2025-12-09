import time
import math
import numpy as np
from collections import namedtuple
from typing import List

from aoc.base_solution import BaseSolution
from aoc.data_structures import Matrix
from aoc.io import IO

State = namedtuple("State", ["position", "velocity"])


class Solution(BaseSolution):

    def init(self) -> None:
        self.states: List[State] = []
        for line in IO.load_lines(self.filename):
            raw_position, raw_velocity = line.split(" ")
            position_x, position_y = raw_position[2:].split(",")
            velocity_x, velocity_y = raw_velocity[2:].split(",")
            position = np.array((int(position_x), int(position_y)))
            velocity = np.array((int(velocity_x), int(velocity_y)))
            self.states.append(State(position, velocity))

    def _get_dimensions(self) -> tuple[int, int]:
        return (11, 7) if self.use_example else (101, 103)

    def stage1(self) -> int:
        width, height = self._get_dimensions()
        x_mid, y_mid = width // 2, height // 2
        quadrants = {i: 0 for i in range(1, 5)}
        ticks = 100
        for state in self.states:
            x, y = state.position + ticks * state.velocity
            x, y = x % width, y % height

            if x < x_mid and y < y_mid:
                quadrants[1] += 1
            elif x < x_mid and y > y_mid:
                quadrants[2] += 1
            elif x > x_mid and y < y_mid:
                quadrants[3] += 1
            elif x > x_mid and y > y_mid:
                quadrants[4] += 1

        return math.prod(quadrants.values())

    def _print(self, positions: List[tuple[int, int]], tick: int) -> None:
        width, height = self._get_dimensions()
        grid = Matrix([[" "] * width for _ in range(height)])
        for x, y in positions:
            grid[y][x] = "*"

        # Clear screen and move cursor to top-left
        print("\033[2J\033[H", end="")
        print(f"\n\nIteration {tick}")
        print(grid)
        time.sleep(0.5)

    def stage2(self) -> int:
        width, height = self._get_dimensions()
        curr_positions = [state.position for state in self.states]
        tick = 0
        while True:
            tick += 1
            for i, (state, position) in enumerate(zip(self.states, curr_positions)):
                x, y = position + state.velocity
                curr_positions[i] = (x % width, y % height)

            if len(curr_positions) == len(set(curr_positions)):
                self._print(curr_positions, tick)


if __name__ == "__main__":
    Solution.main()
