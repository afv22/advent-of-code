from collections import deque
from typing import List

from aoc.base_solution import BaseSolution
from aoc.data_structures.matrix import VECTORS_4
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        self.map = IO.load_matrix(self.filename, int)

    def _find_trailheads(self) -> List[tuple[int, int]]:
        trailheads = []
        for i, row in enumerate(self.map.rows):
            for j, col in enumerate(row):
                if not col:
                    trailheads.append((i, j))

        return trailheads

    def _plan_next_steps(
        self, q: deque, row: int, col: int, next_altitude: int
    ) -> None:
        for row_delta, col_delta in VECTORS_4:
            new_row, new_col = row + row_delta, col + col_delta
            if self.map.is_valid(new_row, new_col) and self.map[new_row][new_col]:
                q.append((next_altitude, (new_row, new_col)))

    def stage1(self) -> int:
        trailheads = self._find_trailheads()
        total_score = 0
        for trailhead in trailheads:
            q, peaks = deque([(0, trailhead)]), set()
            while q:
                altitude, (row, col) = q.popleft()
                if altitude == 9:
                    peaks.add((row, col))
                else:
                    self._plan_next_steps(q, row, col, altitude + 1)

            total_score += len(peaks)

        return total_score

    def stage2(self) -> int:
        trailheads = self._find_trailheads()
        total_rating = 0
        for trailhead in trailheads:
            q = deque([(0, trailhead)])
            while q:
                altitude, (row, col) = q.popleft()
                if altitude == 9:
                    total_rating += 1
                else:
                    self._plan_next_steps(q, row, col, altitude + 1)

        return total_rating


if __name__ == "__main__":
    Solution.main()
