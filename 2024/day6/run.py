from typing import Optional

from aoc.base_solution import BaseSolution
from aoc.data_structures.matrix import VECTORS_4
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        self.grid = IO.load_matrix(self.filename)

    def _initial_position(self) -> tuple[int, int]:
        for row, col in self.grid.coordinates:
            if self.grid[row][col] == "^":
                return (row, col)
        return (-1, -1)

    def _tick(
        self,
        row: int,
        col: int,
        direction: int,
        obstacle: Optional[tuple[int, int]] = None,
    ) -> tuple[int, int, int, bool]:
        row_delta, col_delta = VECTORS_4[direction]
        new_row, new_col = row + row_delta, col + col_delta
        if not self.grid.is_valid(new_row, new_col):
            return row, col, direction, False

        if self.grid[new_row][new_col] == "#" or (
            obstacle and new_row == obstacle[0] and new_col == obstacle[1]
        ):
            direction = (direction + 1) % 4
        else:
            row, col = new_row, new_col

        return row, col, direction, True

    def stage1(self) -> int:
        (row, col), direction = self._initial_position(), 3  # UP
        visited = set()
        inbounds = True
        while inbounds:
            visited.add((row, col))
            row, col, direction, inbounds = self._tick(row, col, direction)

        return len(visited)

    def _creates_loop(self, obstacle_row: int, obstacle_col: int) -> bool:
        (row, col), direction = self._initial_position(), 3
        visited_states = set()
        inbounds = True

        while inbounds:
            state = (row, col, direction)
            if state in visited_states:
                return True

            visited_states.add(state)
            row, col, direction, inbounds = self._tick(
                row, col, direction, (obstacle_row, obstacle_col)
            )

        return False

    def stage2(self) -> int:
        start_row, start_col = self._initial_position()
        row, col, direction = start_row, start_col, 3
        visited = set()
        inbounds = True

        while inbounds:
            visited.add((row, col))
            row, col, direction, inbounds = self._tick(row, col, direction)

        tally = 0
        for obstacle_row, obstacle_col in visited:
            if (obstacle_row, obstacle_col) == (start_row, start_col):
                continue
            if self.grid[obstacle_row][obstacle_col] == "#":
                continue

            if self._creates_loop(obstacle_row, obstacle_col):
                tally += 1

        return tally


if __name__ == "__main__":
    Solution.main()
