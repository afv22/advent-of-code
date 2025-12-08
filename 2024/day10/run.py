from collections import deque
from typing import List

from aoc.base_solution import BaseSolution
from aoc.io import IO


class Solution(BaseSolution):

    def init(self) -> None:
        lines = IO.load_lines(self.filename)
        self.map: List[List[int]] = [[int(n) for n in line] for line in lines]

    def _find_trailheads(self) -> List[tuple[int, int]]:
        trailheads = []
        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                if not col:
                    trailheads.append((i, j))

        return trailheads

    def _plan_next_steps(
        self, q: deque, row: int, col: int, next_altitude: int
    ) -> None:
        if row > 0 and self.map[row - 1][col] == next_altitude:
            q.append((next_altitude, (row - 1, col)))
        if row < len(self.map) - 1 and self.map[row + 1][col] == next_altitude:
            q.append((next_altitude, (row + 1, col)))
        if col > 0 and self.map[row][col - 1] == next_altitude:
            q.append((next_altitude, (row, col - 1)))
        if col < len(self.map[0]) - 1 and self.map[row][col + 1] == next_altitude:
            q.append((next_altitude, (row, col + 1)))

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
